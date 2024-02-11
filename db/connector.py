import mysql.connector

# establish connection to the MySQL database
try:
    conn = mysql.connector.connect(host='localhost',
                                   user='root',
                                   password='assambalers',
                                   database='test')
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your username or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    # create a cursor to execute SQL queries
    cursor = conn.cursor()
    # execute test query
    query = "SELECT * FROM tab"
    cursor.execute(query)
    # fetch and print the results
    for row in cursor.fetchall():
        print(row)
    # close the cursor and connection
    cursor.close()
    conn.close()
