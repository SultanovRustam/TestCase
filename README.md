# TestCase
Тестовое задание
### Стек
- Python
- Django
- PostgreSQL
- nginx
- gunicorn
- Docker
## Запуск проекта

### Начало работы
Клонируйте репозиторий и перейдите в него в командной строке:
```
git clone https://github.com/SultanovRustam/TestCase/
```
```
cd TestCase
```

Установите Docker, используя инструкции с официального сайта:
https://www.docker.com/products/docker-desktop/

- Перейдите в директорию microservice/infra и выполните команды для запуска приложения в контейнерах

    - Собрать и запустить контейнеры:
        ```
        docker-compose up -d
        ```
    - Выполнить миграции:
        ```
        docker-compose exec web python manage.py migrate
        ```
    - Заполнить БД тестовыми данными:
        ```
        docker-compose exec web python manage.py loaddata fixture.json
        ```
    - Остановить контейнеры:
        ```
        docker-compose down -v 
        ```
