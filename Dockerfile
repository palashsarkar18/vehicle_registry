FROM python:3.12

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Install netcat-openbsd
RUN apt-get update && apt-get install -y netcat-openbsd

# Copy the requirements file
COPY requirements.txt /app/

# Install dependencies
RUN pip install -r requirements.txt

# Copy the Django project
COPY . /app/

# Copy wait-for-it and entrypoint scripts
COPY wait-for-it.sh /app/wait-for-it.sh
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/wait-for-it.sh /app/entrypoint.sh

# Expose the port that the Django app runs on
EXPOSE 8000

# Run the entrypoint script
ENTRYPOINT ["/app/wait-for-it.sh", "db:5432", "--", "/app/entrypoint.sh"]
