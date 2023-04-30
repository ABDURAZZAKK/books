# Books

# ENDPOINTS

http://localhost:8000/

### Авторы

GET /authors/ 
POST /authors/

### Книги

GET /books/<pk:int>
GET /books/
POST /books/
PUT /books/<pk:int>
DELETE /books/<pk:int>

# ЗАПУСК ПРОЕКТА

```bash
docker compose up
```

# или


## Установка виртуального окружения:
```bash
python -m venv venv
```

## Запуск вертуального окружения:

### Unix
```bash
. venv/bin/activete
```

### Windows
```bash
venv/Scripts/activete
```

## Установка зависимостей:

```bash
pip install -r requirements.txt
```

## Запуск миграций:
```bash
python manage.py migrate
```

## Запуск проекта:
```bash
python manage.py runserver
```