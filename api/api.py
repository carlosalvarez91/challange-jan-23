import time
from flask import Flask, jsonify, request
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

@app.route('/api/insert_data', methods=["POST"])
def insert_data():
    data = request.get_json()
    json_body = [
        {
            "measurement": "events",
            "fields": {
                "value": data['value']
            }
        }
    ]

    client.write_points(json_body)
    result = client.query('SELECT * FROM events')
    return jsonify(list(result.get_points()))

@app.route('/api/query_data')
def query_data():
    result = client.query('SELECT * FROM events')
    return jsonify(list(result.get_points()))