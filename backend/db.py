import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="swiggy_da",
        autocommit=False,
        connection_timeout=10,
        buffered=True
    )
