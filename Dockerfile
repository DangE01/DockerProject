#Parent Image
FROM python:3.7-stretch

WORKDIR /app

COPY . app.py /app/
# Install packages from requirements.txt
# hadolint ignore=DL3013
RUN pip install --upgrade pip &&\
    pip install --trusted-host pypi.python.org -r requirements.txt
    
CMD ["echo", "Welcome to my Docker Project"]
CMD ["python3", "app.py"]