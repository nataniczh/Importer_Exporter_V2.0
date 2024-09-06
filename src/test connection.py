import sqlite3
from sqlcipher3 import dbapi2 as sqlcipher

conn = sqlcipher.connect("D:\\section_database.db")
cursor = conn.cursor()


cursor.execute("PRAGMA key = 'kAJvgweieFPqt8S2sMWmbNS3twkRhv7s';")


try:
    cursor.execute("SELECT * FROM SectionSeries WHERE id = 2255;")
    print(cursor.fetchall())
except sqlite3.DatabaseError as e:
    print("An error occurred:", e)


conn.close()