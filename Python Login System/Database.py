import mysql.connector

def open():
    global conn
    global cursor
    conn = mysql.connector.connect(
        host='localhost',
        database='projectdb',
        user='root',
        password='*******',
        auth_plugin='mysql_native_password'
    )
    cursor = conn.cursor()

def close():
    conn.commit()  # Save changes to the database
    cursor.close()
    conn.close()

def login(username, password):
    open()  
    query = "SELECT * FROM igldetails WHERE username=%s AND password=%s"
    cursor.execute(query, (username, password))   
    rec = cursor.fetchall()
    close()   
    return len(rec) > 0

def insert(username, password):
    open()
    sql = "INSERT INTO igldetails (username, password) VALUES (%s, %s)"
    values = (username, password)
    cursor.execute(sql, values)
    close()
