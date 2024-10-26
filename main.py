import os
import psycopg2
from psycopg2 import OperationalError

def add_question(conn, question, answer, category):
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO questions (question, answer, category) VALUES (%s, %s, %s)",
            (question, answer, category)
        )
        conn.commit()

def get_all_questions(conn):
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM questions")
        questions = cur.fetchall()
        print("ALL")
        for question in questions:
            print(question)

def main():
    DATABASE_URL = os.getenv('DATABASE_URL')
    try:
        conn = psycopg2.connect(DATABASE_URL)
        add_question(conn, "What is the capital of France?", "Paris", "Geography")
        get_all_questions(conn)
    except OperationalError as e:
        print(f"Ошибка подключения к PostgreSQL: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    main()