# Use an official Python runtime as the base ima
FROM python:3.9-slim

ARG EMAIL_PASSWORD
ARG EMAIL_SENDER
ARG EMAIL_REC

ENV EMAIL_PASSWORD=$EMAIL_PASSWORD
ENV EMAIL_SENDER=$EMAIL_SENDER
ENV EMAIL_REC=$EMAIL_REC

# Set the working directory in the container
WORKDIR /app

# Install the dependencies specified in requirements.txt
RUN pip install python-decouple

# Copy the rest of the application files to the working directory
COPY . .

# Command to run the Python script
CMD ["python", "send_email.py"]
