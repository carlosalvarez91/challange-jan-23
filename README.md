### Random event generator

This app allows the user to create random events allocated between now and one week before and after and display the average of events per day/hour/minute.

<img width="878" alt="image" src="https://user-images.githubusercontent.com/17145410/212391496-318e1339-e85b-4b0f-8ccb-b2b181bde728.png">


This project starts from a boilerplate that has been cloned from https://github.com/miguelgrinberg/react-flask-app and simplified.

### Technologies 

- Frontend: React, bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

- Backend: Flask

- Database: InfluxDB v.1.8

### Demo: 
https://www.loom.com/share/e2a97c085baa416cbde3cf8caa3bb63e


### Steps to get it up and running:


##### Install Backend:

1. create venv inside /api directory:
```
$ python3 -m venv venv
```

2. activate virtualenv: 
```
$ source api/venv/bin/activate
```

3. install packages
```
$ pip install -r requirements.txt
```

##### Install Frontend:

```
$ npm install
```


##### Run Project:

1. Run backend
```
$ yarn start-api
```

2. Run Frontend

```
$ yarn start
```

##### InfluxDB
We will use any version previous to 2, in my machine I'm using 1.8

Installation (mac):
```
brew install influxdb@1
```

run influx:
```
$ influxd 
```

run cli:
```
$ influx
```

create db

```
CREATE DATABASE test
```

create admin user

```
CREATE USER admin WITH PASSWORD 'password' WITH ALL PRIVILEGES
```

