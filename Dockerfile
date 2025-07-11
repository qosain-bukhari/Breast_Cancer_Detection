# Use Python 3.10 as base
FROM python:3.10

# Set working directory in container
WORKDIR /app

# Copy everything into container
COPY . /app

# Install required Python packages
RUN pip install --default-timeout=100 --no-cache-dir -r requirements.txt


# Expose port 8501 for Streamlit
EXPOSE 8501

# Start the app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
