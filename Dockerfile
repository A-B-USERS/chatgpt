# Base image
FROM python:3.10

# Set working directory inside container
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Train model automatically on build (optional)
RUN python model/train.py

# Set Python path so 'app' module is recognized
ENV PYTHONPATH=/app

# Run the FastAPI app using uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
# Base image
FROM python:3.10

# Set working directory inside container
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Train model automatically on build (optional)
RUN python model/train.py

# Set Python path so 'app' module is recognized
ENV PYTHONPATH=/app

# Run the FastAPI app using uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

