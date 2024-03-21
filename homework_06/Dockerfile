FROM python:3.11-alpine3.19

WORKDIR /app

RUN pip install --upgrade pip

RUN pip install Flask \
    psycopg2-binary \
    Flask-SQLAlchemy \
    asyncpg \
    gunicorn



COPY . .

EXPOSE 8000

CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8000"]
