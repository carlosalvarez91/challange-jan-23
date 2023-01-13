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



InfluxDB, we will use any version previous to 2, in my machine I'm using 1.8

installation (mac):
brew install influxdb@1

Setup influx:

run influx:
$ influxd 

run cli:
$ influx

create db

CREATE DATABASE test

create admin user

CREATE USER admin WITH PASSWORD '<password>' WITH ALL PRIVILEGES

