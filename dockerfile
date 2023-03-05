# Указываем базовый образ
FROM python:3.8-slim-buster

# Устанавливаем рабочую директорию в контейнере
WORKDIR /run

# Копируем зависимости в контейнер
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код в контейнер
COPY . .

# Указываем команду для запуска приложения
CMD [ "python", "run.py" ]