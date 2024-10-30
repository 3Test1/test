import psycopg2

def connect():
    conn = psycopg2.connect(
        dbname='myprojectdb',
        user='your_username',
        password='your_password',
        host='localhost'
    )
    return conn
