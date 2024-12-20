FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the local package and project files to the working directory
COPY requirements.txt ./
COPY app/ ./app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME=World

# Run app.py when the container launches
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]