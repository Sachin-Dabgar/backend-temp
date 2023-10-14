# Use the official Python base image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install -y libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install dependencies
RUN pip install  -r requirements.txt

# Copy the Django project files to the container's working directory
COPY . .

# RUN python manage.py makemigrations
# RUN python manage.py migrate

# Expose the port the Django app is running on
EXPOSE 8000

# Command to run the Django app using Gunicorn server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "ecom.wsgi:application"]
