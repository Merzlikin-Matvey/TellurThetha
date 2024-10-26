# Dockerfile
FROM python:3.12

# Установка зависимостей
RUN apt-get update && apt-get install -y postgresql-client

# Установка необходимых Python пакетов
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копирование исходного кода
COPY . /app
WORKDIR /app

# Команда для запуска приложения
CMD ["python", "main.py"]