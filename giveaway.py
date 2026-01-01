class Giveaway:
    def __init__(self, 
                 id: int, 
                 title: str, 
                 worth: str, 
                 thumbnail: str, 
                 image: str, 
                 description: str, 
                 instructions: str, 
                 open_giveaway_url: str, 
                 published_date: str, 
                 type: str, 
                 platforms: str, 
                 end_date: str, 
                 users: str, 
                 status: str, 
                 gamerpower_url: str, 
                 open_giveaway: str) -> None:
        self.id: int = id
        self.title: str = title
        self.worth: str = worth
        self.thumbnail: str = thumbnail
        self.image: str = image
        self.description: str = description
        self.instructions: str = instructions
        self.open_giveaway_url: str = open_giveaway_url
        self.published_date: str = published_date
        self.type: str = type
        self.platforms: str = platforms
        self.end_date: str = end_date
        self.users: str = users
        self.status: str = status
        self.gamerpower_url: str = gamerpower_url
        self.open_giveaway: str = open_giveaway
