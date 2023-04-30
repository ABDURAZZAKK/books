FROM python:3


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN python -m pip install --upgrade pip


WORKDIR /app
COPY . .

RUN pip install -r requirements.txt && python manage.py migrate