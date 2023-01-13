import time
from flask import Flask, jsonify, request
from flask_cors import CORS
from influxdb import InfluxDBClient
from datetime import datetime, timedelta
import random

# Flask app
app = Flask(__name__, static_folder='../build', static_url_path='/')
CORS(app, origins=['http://localhost:3000']) 

# Influx
client = InfluxDBClient(host='0.0.0.0', port=8086, username='admin', password='password', database='test')

# Router
@app.errorhandler(404)
def not_found(e):
    return app.send_static_file('index.html')

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/api/insert_data', methods=["POST"])
def insert_data():
    data = request.get_json()
    # get the current time
    now = datetime.now()
    # set the time range, one week before and after
    start_time = now - timedelta(weeks=1)
    end_time = now + timedelta(weeks=1)
    # generate a random time within the range
    random_time = start_time + timedelta(seconds=random.randint(0, int((end_time - start_time).total_seconds())))
    random_time_iso = random_time.isoformat()
    json_body = [
        {
            "measurement": "events",
            "time": random_time_iso,
            "fields": {
                "value": data['value']
            }
        }
    ]
    client.write_points(json_body)
    result = client.query('SELECT value FROM events')
    return jsonify(list(result.get_points()))

@app.route('/api/query_data/<window>')
def query_data_avg(window):
    print('.... window ',window)
    time = '1m' # default
    if window == 'day':
        time = '1d'
    if window == 'hour':
        time = '1h'
    if window == 'minute':
        time = '1m'
    if window == 'all':
        result = client.query('SELECT value FROM events')
        return jsonify(list(result.get_points()))

    query = f'''SELECT MEAN(value) as value FROM events GROUP BY time({time})'''
    print(query)
    result = client.query(query)
    return jsonify(list(result.get_points()))