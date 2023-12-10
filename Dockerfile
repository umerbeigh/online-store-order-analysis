# Stage 1: Build
FROM python:3.8 AS builder

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Stage 2: Run Tests
FROM builder AS test-runner

CMD ["python", "-m", "unittest", "test_orders.py"]

# Stage 3: Run Program
FROM builder AS program-runner

# Expose any necessary ports
# EXPOSE 80

# Run your Python script when the container launches
CMD ["python", "./order_analysis.py"]

