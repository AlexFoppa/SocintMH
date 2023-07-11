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

def clean_table():
    with conn:
        c.execute("""DROP TABLE IF EXISTS instagramTwins""")
        create_table_instagramTwins()

def insert_twin(person):
    with conn:  
        c.execute("INSERT INTO instagramTwins (name, doc, email, history) VALUES (:name, :doc, :email, :history)", 
                {'name':person.name, 'text':person.doc, 'email':person.exteemailnsion,'history':person.history})
        return c.lastrowid

def get_all_persons():
    c.execute("SELECT * FROM instagramTwins")
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

