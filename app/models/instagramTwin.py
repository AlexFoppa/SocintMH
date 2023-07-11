class InstagramTwin:

    def __init__(self, personId, instagramId, account_type, media_count,username) -> None:
        self.id = 0
        self.personId = personId
        self.instagramId = instagramId
        self.account_type = account_type
        self.media_count = media_count
        self.username = username

class InstagramFeedPublication:

    def __init__(self, personId, instagramId, caption, media_type, media_url, permalink, timestamp, username) -> None:
        self.id = 0
        self.personId = personId
        self.instagramId = instagramId
        self.caption = caption
        self.media_type = media_type
        self.media_url = media_url
        self.permalink = permalink
        self.timestamp = timestamp
        self.username = username