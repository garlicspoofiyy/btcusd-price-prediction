# FROM python:3.12.7-slim

# RUN apt-get update && apt-get install -y \
#     gcc \
#     g++ \
#     make \
#     && apt-get clean \
#     && rm -rf /var/lib/apt/lists/*

# RUN pip install pipenv

# WORKDIR /app

# COPY ["./Pipfile", "./Pipfile.lock", "./"]

# RUN pipenv install --system --deploy 

# COPY ["btc-prediction/", "./btc-prediction/"]

# COPY ["btc-prediction/app.py", "./"]

# CMD ["python", "app.py"]

# EXPOSE 9696

# ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "app:app"]

FROM python:3.12.7-slim

RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    make \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install pipenv

WORKDIR /app

COPY ["./Pipfile", "./Pipfile.lock", "./"]

RUN pipenv install --system --deploy 

# Copy the entire btc-prediction directory, including templates
COPY ["btc-prediction/", "./btc-prediction/"]

# Install Gunicorn
RUN pip install gunicorn

# Run the app using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:9696", "btc-prediction.app:app"]

EXPOSE 9696