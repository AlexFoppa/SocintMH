import sqlite3

conn = sqlite3.connect('socintmh.db', check_same_thread=False)

c = conn.cursor()

def create_table_person():
    with conn:        
        c.execute("""CREATE TABLE persons (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name text,
            doc text,
            email text,
            history text 
            )""")

def clean_table():
    with conn:
        c.execute("""DROP TABLE IF EXISTS persons""")
        create_table_person()

def insert_person(person):
    with conn:  
        c.execute("INSERT INTO persons (name, doc, email, history) VALUES (:name, :doc, :email, :history)", 
                {'name':person.name, 'text':person.doc, 'email':person.email,'history':person.history})
        return c.lastrowid

def get_all_persons():
    c.execute("SELECT * FROM persons")
    return c.fetchall()

def get_person_by_name(name):
    c.execute("SELECT * FROM persons WHERE name=:name", {'name': name})
    return c.fetchall()

def get_person_by_id(id):
    c.execute("SELECT * FROM person WHERE id=:id", {'id': id})
    return c.fetchall()

