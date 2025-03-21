FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code into the container
COPY src/ ./src/
COPY data/ ./data/
COPY notebooks/ ./notebooks/
COPY presentation/ ./presentation/

# Command to run the application
CMD ["python", "src/model/train_model.py"]