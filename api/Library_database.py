import sqlite3
from fastapi import FastAPI
from pydantic import BaseModel

conn = sqlite3.connect('Library_database.db')

cursor = conn.cursor()

cursor.execute(''' 
               CREATE TABLE IF NOT EXISTS datos (
               id INTEGER PRYMARY KEY AUTOINCREMENT,
               titulo TEXT NOT NULL,
               artista TEXT NOT NULL,
               posicion INTEGER
               )''')

conn.commit()
conn.close()


#%%
def read_csv_file(csv_file):
    with open(csv_file, newlinw='') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data

def inawert_data_to_ranking_table(data):
    conn = sqlite3.connect("datos.db")
    cursor = conn.cursor()

    for row in data:
        cursor.execute()

    conn.commit()
    conn.close()

    #%%
   
