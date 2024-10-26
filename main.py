import os
import psycopg2
from psycopg2 import OperationalError

def check_postgres_connection():
    try:
        connection = psycopg2.connect(
            host=os.getenv('DB_HOST', 'localhost'),
            port=os.getenv('DB_PORT', '5432'),
            database=os.getenv('DB_NAME', 'mydatabase'),
            user=os.getenv('DB_USER', 'user'),
            password=os.getenv('DB_PASSWORD', 'password')
        )
        cursor = connection.cursor()
        cursor.execute("SELECT 1;")
        result = cursor.fetchone()
        if result:
            print("PostgreSQL работает корректно.")
        cursor.close()
        connection.close()
    except OperationalError as e:
        print(f"Ошибка подключения к PostgreSQL: {e}")

if __name__ == "__main__":
    check_postgres_connection()