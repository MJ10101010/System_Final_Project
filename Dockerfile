# Use official Python image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /src

# Copy dependency file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

# Default command to run the app
# CMD ["python", "src/app.py"]

CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "5000"]
