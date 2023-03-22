# yamdb_final
yamdb_final
[![api_yamdb_workflow](https://github.com/quickest5/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)](https://github.com/quickest5/yamdb_final/actions/workflows/yamdb_workflow.yml)

http://practicum-back.ddns.net/redoc/

https://hub.docker.com/repository/docker/killtsunami/api_yamdb/general
# Описание проекта
Проект YaMDb предназначен для хранения информации о произведениях и отзывов пользователей на эти произведения. Администратор может добавлять произведения, категории и жанры, а пользователи могут оставлять отзывы, комментарии и ставить оценки произведениям.

## Шаблон env-файла
Для запуска проекта необходимо создать файл .env в папке infra в папке проекта с следующим содержимым:
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=<postgres_username>
POSTGRES_PASSWORD=<postgres_password>
DB_HOST=db
DB_PORT=5432
```
Замените <postgres_username> и <postgres_password> на свои значения.

# Команды для запуска приложения в контейнерах
## Установка Docker
https://docs.docker.com/engine/install/
Перед запуском приложения необходимо установить Docker и Docker Compose. Инструкции по установке можно найти по ссылке
## Запуск приложения
Для запуска приложения в контейнерах выполните следующие команды:

```
docker-compose up -d --build
docker-compose exec web python manage.py migrate
```
Для создания суперпользователя и для работы статики выполните команды:
```
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --no-input
```

# Команда для заполнения базы данными
Для заполнения базы данных предварительно необходимо создать суперпользователя (см. предыдущий раздел).
Затем выполните следующую команду:

```
docker-compose exec web python manage.py loaddata fixtures.json
```
Файл fixtures.json содержит тестовые данные для заполнения базы данных.