
import sqlite3

conn = sqlite3.connect('socintmh.db', check_same_thread=False)

c = conn.cursor()

def create_table():
    with conn:
        c.execute("""CREATE TABLE audios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name text,
            text text,
            extension text,
            type text, 
            path text,
            hashMD5 text,
            hashSHA256 text,
            duration text,
            creationDate text,
            modificationDate text,
            size text
            )""")
    
def clean_table():
    with conn:
        c.execute("""DROP TABLE IF EXISTS audios""")
        create_table()

def insert_audio(audio):
    with conn:  
        c.execute("INSERT INTO audios (name, text, extension, type, path, hashMD5, hashSHA256, duration, creationDate, modificationDate, size) VALUES (:name, :text, :extension, :type, :path, :hashMD5,:hashSHA256, :duration, :creationDate, :modificationDate, :size)", 
                {'name':audio.name, 'text':audio.text, 'extension':audio.extension,'type':audio.type,'path':audio.path,'hashMD5':audio.hashMD5,'hashSHA256':audio.hashSHA256, 'duration':audio.duration, 'creationDate':audio.creationDate, 'modificationDate':audio.modificationDate, 'size':audio.size })
        return c.lastrowid

def get_all_audio():
    c.execute("SELECT * FROM audios")
    return c.fetchall()

def get_audio_by_name(name):
    c.execute("SELECT * FROM audios WHERE name=:name", {'name': name})
    return c.fetchall()

def get_audio_by_id(id):
    c.execute("SELECT * FROM audios WHERE id=:id", {'id': id})
    return c.fetchall()

