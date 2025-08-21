# web/Dockerfile
FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy only what's needed for the Dash app
COPY app.py .
# CSV will be mounted via volume

EXPOSE 8050
CMD ["python", "app.py"]
