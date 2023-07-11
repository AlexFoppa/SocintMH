class InstagramTwin:

    def __init__(self, personId, instagramId, account_type, media_count,username) -> None:
        self.id = 0
        self.personId = personId
        self.instagramId = instagramId
        self.account_type = account_type
        self.media_count = media_count
        self.username = username

    def get_data(self):
        return  self.id,self.personId,self.instagramId,self.account_type,self.media_count,self.username