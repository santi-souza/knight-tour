# Use the official Python 3 image as the base
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install necessary Python libraries
RUN pip install --no-cache-dir -r requirements.txt

# Install Graphviz for generating graphs
RUN apt-get update && apt-get install -y graphviz && rm -rf /var/lib/apt/lists/*

# Expose any ports the app runs on (if applicable)
# Example: Uncomment the line below if your app uses a web server
# EXPOSE 5000

# Command to run the script when the container starts
ENTRYPOINT ["python", "knight_tour.py"]
CMD ["--start", "a1", "--end", "h8"]


#######

# HOW TO CREATE THE DOCKER IMAGE
# Build the docker image
# docker build -t knight_tour .

# Run the container
# docker run --rm knight_tour

# Optional: If the program generates files like .dot files or images, map a volume to persist these:
# docker run --rm -v $(pwd)/output:/app/output knight_tour


