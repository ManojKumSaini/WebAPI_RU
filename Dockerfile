# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory to /app
WORKDIR /src

# Copy requirements.txt into the container at /app
COPY src/requirements.txt ./requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY src/ .
# Make port 8501 available to the world outside this container
EXPOSE 80

# Run app.py when the container launches
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=80", "--server.address=0.0.0.0"]
