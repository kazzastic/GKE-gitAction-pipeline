# Use an official Python runtime as the base imag
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install the dependencies specified in requirements.txt
RUN pip install python-decouple

# Copy the rest of the application files to the working directory
COPY . .

# Command to run the Python script
CMD ["python", "send_email.py"]
