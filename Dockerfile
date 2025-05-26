
FROM python:3.9-slim
WORKDIR /app
COPY process.py /app/
RUN pip install pandas
CMD ["python", "process.py"]
