# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies listed in requirements.txt
RUN pip install -r requirements.txt

# Copy the current project directory into the container
COPY . .

# Expose port 8000 for the Django development server
EXPOSE 8000

# Command to start the Django development server on port 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
