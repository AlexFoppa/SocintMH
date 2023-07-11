import sqlite3

conn = sqlite3.connect('socintmh.db', check_same_thread=False)

c = conn.cursor()

def create_table_instagramTwins():
    with conn:        
        c.execute("""CREATE TABLE instagramTwins (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            personId INTEGER,
            instagramId INTEGER,
            account_type text,
            media_count text,
            username text     
            )""")
        
        c.execute("""CREATE TABLE instagramFeedPublications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            personId INTEGER,
            instagramId INTEGER,
            caption text,
            captionSentimentPolarity,
            media_type text,
            media_url text,
            permalink text,
            timestamp text,
            username text     
            )""")

def clean_tables_instagram():
    with conn:
        c.execute("""DROP TABLE IF EXISTS instagramTwins""")
        c.execute("""DROP TABLE IF EXISTS instagramFeedPublications""")
        create_table_instagramTwins()

def insert_twin(instagramTwin):
    with conn:  
        c.execute("INSERT INTO instagramTwins (personId, instagramId, account_type, media_count, username) VALUES (:personId, :instagramId, :account_type, :media_count, :username)", 
                {'personId':instagramTwin.personId, 'instagramId':instagramTwin.instagramId, 'account_type':instagramTwin.account_type,'media_count':instagramTwin.media_count,'username':instagramTwin.username})
        return c.lastrowid

def insert_publication(instagramFeedPublication):
    with conn:  
        c.execute("INSERT INTO instagramFeedPublications (personId,instagramId,caption,captionSentimentPolarity,media_type,media_url,permalink,timestamp,username) VALUES (:personId,:instagramId,:caption,:captionSentimentPolarity,:media_type,:media_url,:permalink,:timestamp,:username)", 
                {'personId':instagramFeedPublication.personId, 'instagramId':instagramFeedPublication.instagramId, 'caption':instagramFeedPublication.caption, 'captionSentimentPolarity': instagramFeedPublication.captionSentimentPolarity,'media_type':instagramFeedPublication.media_type,'media_url':instagramFeedPublication.media_url,'permalink':instagramFeedPublication.permalink,'timestamp':instagramFeedPublication.timestamp,'username':instagramFeedPublication.username})
        return c.lastrowid

def get_all_twins():
    c.execute("SELECT * FROM instagramTwins")
    return c.fetchall()

def get_all_pubs():
    c.execute("SELECT * FROM instagramFeedPublications")
    return c.fetchall()

def get_twin_by_username(username):
    c.execute("SELECT * FROM instagramTwins WHERE username=:username", {'username': username})
    return c.fetchall()

def get_twin_by_personId(personId):
    c.execute("SELECT * FROM instagramTwins WHERE personId=:personId", {'personId': personId})
    return c.fetchall()

def get_twin_by_instagramId(instagramId):
    c.execute("SELECT * FROM instagramTwins WHERE instagramId=:instagramId", {'instagramId': instagramId})
    return c.fetchall()

