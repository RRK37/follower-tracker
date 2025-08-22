FROM mcr.microsoft.com/playwright/python:v1.48.0-focal

WORKDIR /app

# Copy and install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the scripts
COPY get-followers.py .
COPY worker_loop.py .
COPY username.txt .

# Run the loop instead of the single script
CMD ["python", "worker_loop.py"]
