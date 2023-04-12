# Use the official Python base image
FROM python:3.8

# Set the working directory in the container
WORKDIR /backend

# Copy the contents of the current directory to the container
COPY . .

# Install the Python dependencies
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose the port on which the app will run
EXPOSE 8000

# Start the FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
