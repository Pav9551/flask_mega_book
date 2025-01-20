# Выкачиваем из dockerhub образ с python версии 3.11
FROM python:3.11
# Устанавливаем рабочую директорию для проекта в контейнере
WORKDIR /microblog
# Скачиваем/обновляем необходимые библиотеки для проекта 
COPY requirements.txt /microblog
RUN pip3 install --upgrade pip -r requirements.txt
# |ВАЖНЫЙ МОМЕНТ| копируем содержимое папки, где находится Dockerfile, 
# в рабочую директорию контейнера
COPY . /microblog

# Устанавливаем порт, который будет использоваться для сервера
EXPOSE 5000

CMD ["gunicorn","-w", "4", "--bind", "0.0.0.0:5000","wsgi:app"]
