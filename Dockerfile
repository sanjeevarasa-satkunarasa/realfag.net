# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y \
    ocrmypdf \
    tesseract-ocr-nor \
    && apt-get clean

# Copy the project files to the container
COPY . /app

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Expose the port the app runs on
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
