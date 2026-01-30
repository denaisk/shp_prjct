FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY data_generator.py .
CMD ["python", "data_generator.py"]