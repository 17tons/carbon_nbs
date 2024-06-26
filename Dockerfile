# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /Users/andreagonelli/docker-curriculum/ml_docker
RUN apt-get update && apt-get install -y gdal-bin\
    build-essential \
    g++ \
    python3-dev \
    libgdal-dev

# Copy the current directory contents into the container at /Users/andreagonelli/docker-curriculum/ml_docker
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run app.py when the container launches
CMD ["python", "./app.py"]