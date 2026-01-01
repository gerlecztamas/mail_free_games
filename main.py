from games import collect_todays_free_games, fetch_giveaways
from mail import convert_games_to_mail_body, send_email

def main():
    fetched_giveaways = fetch_giveaways()

    if len(fetched_giveaways):
        todays_free_games = collect_todays_free_games(fetched_giveaways)

        if len(todays_free_games):
            send_email(convert_games_to_mail_body(todays_free_games))

if __name__ == "__main__":
    main()