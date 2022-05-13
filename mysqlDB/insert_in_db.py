import mysql.connector


def get_mysql_insert_query():
    return """INSERT table1 (
                            issue_id, title, created_at, number, body, state, commits
                            ) VALUES (%s, %s, %s, %s, %s, %s, %s) """

# MySQL connection
connection = mysql.connector.connect(host="localhost", database="my1stmysqldb",\
     user="root",password="youhuanMihua123!")
cursor = connection.cursor()

try:
    mySql_insert_query = get_mysql_insert_query()
    cursor.execute(mySql_insert_query, tuple((888, "my title", "created at: some time", 
    888, "body text", "closed state", 18)))
    connection.commit()

    # inserted_records += 1
    # print(cursor.rowcount, f"Record inserted successfully into {CATEGORIES[category]} table")

except mysql.connector.Error as error:
    print("Failed to insert record into MySQL table {}".format(error))

# Close connection to MySQL
if connection and connection.is_connected():
    cursor.close()
    connection.close()
    print("MySQL connection is closed")
