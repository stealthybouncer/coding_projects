# Use an official Python runtime as a parent image
FROM python:3.13-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y build-essential

# Copy the pyproject.toml and poetry.lock files to the container
COPY pyproject.toml poetry.lock* /app/

# Install Poetry
RUN pip install poetry

# Install dependencies
RUN poetry install --no-root

# Copy the current directory contents into the container at /app
COPY . /app

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run the application
CMD ["poetry", "run", "python", "-m", "coding_projects.main"]

# Run Jupyter Notebook if included

CMD ["poetry", "run", "python", "-m", "coding_projects.main"]


