from server.database_adapter import Adapter
from server.config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD

class Question:
    def __init__(self, id: int, question: str, answer: str, category: str):
        self.id = id
        self.question = question
        self.answer = answer
        self.category = category

    def __str__(self):
        return f"Question: {self.question}, Answer: {self.answer}, Category: {self.category}"

    def __repr__(self):
        return self.__str__()

    def check_answer(self, answer: str):
        return self.answer.lower() == answer.lower()

    def to_dict(self):
        return {
            "id": self.id,
            "question": self.question,
            "answer": self.answer,
            "category": self.category
        }

    @staticmethod
    def from_dict(data: dict):
        return Question(
            id=data["id"],
            question=data["question"],
            answer=data["answer"],
            category=data["category"]
        )

    @staticmethod
    def question_from_db(id: int):
        adapter = Adapter(
            host=DB_HOST,
            port=DB_PORT,
            sslmode='disable',
            dbname=DB_NAME,
            schema_name='public',
            user=DB_USER,
            password=DB_PASSWORD,
            target_session_attrs='read-write'
        )
        adapter.connect()
        data = adapter.select('questions')
        for row in data:
            if row[0] == id:
                return Question(id=row[0], question=row[1], answer=row[2], category=row[3])
        return None

    def save_to_db(self):
        adapter = Adapter(
            host=DB_HOST,
            port=DB_PORT,
            sslmode='disable',
            dbname=DB_NAME,
            schema_name='public',
            user=DB_USER,
            password=DB_PASSWORD,
            target_session_attrs='read-write'
        )
        adapter.connect()
        data = {
            'question': self.question,
            'answer': self.answer,
            'category': self.category
        }
        adapter.insert('questions', data)