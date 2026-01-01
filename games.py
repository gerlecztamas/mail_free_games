import requests

from giveaway import Giveaway
from dateutil.parser import parse
from datetime import date

API_URL = "https://www.gamerpower.com/api/giveaways?platform=epic-games-store"
GAME_TYPE = "Game"

def fetch_giveaways():
    try:
        response = requests.get(API_URL, timeout=500)
        response.raise_for_status()

        return response.json()
    except Exception as e:
        print(f"Error fetching free games: {e}")
        return []
    
def collect_todays_free_games(response_json) -> list[Giveaway]:
    giveaways = [Giveaway(**item) for item in response_json]

    games = list(filter(became_free_game_today, giveaways))

    return games

def became_free_game_today(giveaway: Giveaway) -> bool:
    return giveaway.type == GAME_TYPE and parse(giveaway.published_date).date() == date.today()