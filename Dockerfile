FROM python:3.11-slim@sha256:dad770592ab3582ab2dabcf0e18a863df9d86bd9d23efcfa614110ce49ac20e4

WORKDIR /app

#add requirements
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

#add src files
COPY . .

#run weather-service
CMD ["python3", "main.py"]