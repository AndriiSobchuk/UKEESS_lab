# Stage 1: Build the C library
FROM python:3.9 AS builder

# Install build dependencies for C library
RUN apt-get update && \
    apt-get install -y gcc

# Copy the C source code
COPY fib.c .

# Compile the C library
RUN gcc -shared -o libfib.so fib.c -fPIC

# Stage 2: Create the final image for the Python application
FROM python:3.9

# Copy the Python application files and C library from previous stage
COPY app.py .
COPY --from=builder /libfib.so /libfib.so

# Set the working directory and command for the container
WORKDIR /app
CMD ["python3", "/app.py"]

