FROM python:3.9-slim
WORKDIR /app
ENV PYTHONUNBUFFERED=1
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "input_service.py"]
