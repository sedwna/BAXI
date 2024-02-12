from datetime import date
import mysql.connector

def insert_into_db(dic):
    conn = mysql.connector.connect(host='localhost',
                                   user='root',
                                   password='assambalers',
                                   database='test',
                                   raise_on_warnings=True)
    cursor = conn.cursor()
    # typing
    if dic.get('type') == 0:
        query = ('') # add format
    cursor.execute(query, dic)
    conn.commit()
    cursor.close()
    conn.close()
