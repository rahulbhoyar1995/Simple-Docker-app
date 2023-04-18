FROM python:3.9-alpine

WORKDIR /app

COPY . /app/

CMD ["python", "main.py"]