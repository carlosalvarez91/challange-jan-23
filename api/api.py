import time
from flask import Flask, jsonify
from flask_cors import CORS
from influxdb import InfluxDBClient


app = Flask(__name__, static_folder='../build', static_url_path='/')
CORS(app, origins=['http://localhost:3000']) 

# Influx
client = InfluxDBClient(host='0.0.0.0', port=8086, username='admin', password='password', database='test')

@app.errorhandler(404)
def not_found(e):
    return app.send_static_file('index.html')


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/api/time')
def get_current_time():
    return {'time': time.time()}
