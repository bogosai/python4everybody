import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

    for row in cur.execute('''SELECT Track.title, Artist.name, Album.title, Genre.name 
        FROM Track 
        JOIN Genre ON Track.genre_id = Genre.ID 
        JOIN Album ON Track.album_id = Album.id 
        JOIN Artist ON Album.artist_id = Artist.id 
        ORDER BY Artist.name LIMIT ?''', (3,)):
        print(row)