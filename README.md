# yamdb_final
yamdb_final
[![api_yamdb_workflow](https://github.com/quickest5/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)](https://github.com/quickest5/yamdb_final/actions/workflows/yamdb_workflow.yml)


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