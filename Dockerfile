# Use a lightweight Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy files
COPY requirements.txt .
COPY math_server.py .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port (Cloud runtimes expect this)
EXPOSE 8000

# Command to run the server
# We use python directly because we added the correct logic in step 1
CMD ["python", "math_server.py"]