FROM python:3.10

WORKDIR /app_fast

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "app.main:app"]