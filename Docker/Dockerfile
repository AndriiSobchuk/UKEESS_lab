FROM python:3.9

# Install build dependencies for C library
RUN apt-get update && \
    apt-get install -y gcc

# Copy the C source code and compile the library
COPY fib.c .
RUN gcc -shared -o libfib.so fib.c -fPIC && \
    cp libfib.so /usr/local/lib/ && \
    ldconfig && \
    chmod +x /usr/local/lib/libfib.so

# Copy the Python application files
COPY app.py .

# Set the working directory and command for the container
WORKDIR /app
CMD ["python3", "/app.py"]

