# Use an official Ubuntu image as a base
FROM ubuntu:20.04

# Set non-interactive environment variable
ENV DEBIAN_FRONTEND=noninteractive

# Update the package lists and install necessary packages
RUN apt-get update && \
    apt-get install -y \
    nodejs \
    npm \
    vim && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /Frontend

# Expose multiple ports
EXPOSE 3000 8000

# Copy the current directory contents into the container
COPY . /Frontend
