# Use an official Python runtime as a parent image
FROM python:3

# Set the working directory
WORKDIR /app

# Copy directory contents into the container
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run app.py when the container launches
CMD ["python", "app.py"]