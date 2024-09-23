FROM python:3.9-slim

# Install CMake and other dependencies
RUN apt-get update && apt-get install -y \
    cmake \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies listed in requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the current project directory into the container
COPY . .

# Command to run your application (update this as needed)
CMD ["python", "your_app.py"]
