# Base image - Python 3.10 on lightweight Linux
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements first (for caching)
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy rest of the code
COPY . .

# Expose port 5000
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]