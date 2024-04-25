FROM python:3.8-slim

# Install necessary dependencies for pyodbc
RUN apt-get update \
    && apt-get install -y gnupg gnupg2 gnupg1 \
    && apt-get install -y curl \
    && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y msodbcsql17 \
    && apt-get install -y unixodbc-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python packages
RUN pip install flask pyodbc

WORKDIR /app
COPY app.py /app

CMD ["python", "app.py"]
