This boilerplate has been cloned from https://github.com/miguelgrinberg/react-flask-app and simplified.

The react app was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

A Flask based API backend was added in the *api* directory.


Install Backend:

1. create venv inside /api directory:

$ python3 -m venv venv

2. activate virtualenv: 

$ source api/venv/bin/activate

3. install packages

$ pip install -r requirements.txt

Install Frontend:

1. npm install


Run Project:

1. Run backend

$ yarn start-api

2. Run Frontend

$ yarn start



InfluxDB

installation (mac):
brew install influxdb
brew install influxdb-cli

setup:
$ influx setup

username=admin
password=password

now let's create a db:
$ influx bucket create --name test, or alternative you can use the ui at http://localhost:8086

