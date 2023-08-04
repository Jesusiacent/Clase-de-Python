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