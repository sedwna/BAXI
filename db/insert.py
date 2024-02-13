import mysql.connector

def insert_into_db(values):
    conn = mysql.connector.connect(host='192.168.1.181',
                                   user='root',
                                   password='assambalers',
                                   database='test')
    cursor = conn.cursor()
    # typing
    # if dic.get('type') == 0:
    query = ('INSERT INTO test.tab(name) VALUES (%(name)s)') # add format
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()
