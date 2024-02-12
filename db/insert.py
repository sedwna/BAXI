import mysql.connector

def insert_into_db(dic):
    try:
        conn = mysql.connector.connect(host='localhost',
                                       user='root',
                                       password='assambalers',
                                       database='test',
                                       raise_on_warnings=True)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('something is wrong with your username or password')
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print('database does not exist')
        else:
            print(err)
    else:
        cursor = conn.cursor()
        if dic.get('type') == 'tab':
            query = ('INSERT INTO test.tab(name) VALUES (%(name)s);')
        cursor.execute(query, dic)
        conn.commit()
        cursor.close()
        conn.close()
