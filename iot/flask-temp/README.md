
# Introduction

This is a Flask application to server DS18B20 temperature sensor measurements as REST endpoint http://localhost:5001/get-temp

# Setup

It is recommended to create virtual environment (venv) for the application.
This helps to isolate the dependencies outside OS limitations.

## To initialize the VENV environment for the application:

````
cd <app directory>
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
echo "... OR: pip install flask gunicorn"
````

## Run the application

Activate virtual environment:
````
source venv/bin/activate
<myapp/venv/bin>/gunicorn --bind 0.0.0.0:5001 app:app
````

## Test REST endpoint

````
curl http://localhost:5001/get-temp
````

# Misc 

## Generating configuration 

If there is a need to collect the Python module dependencies to a configuration file:
````
pip freeze > requirements.txt
````

