from flask import Flask, jsonify, request
from flask_cors import CORS
from influxclient import client
from utils import get_random_time

# Flask app
app = Flask(__name__, static_folder='../build', static_url_path='/')
CORS(app, origins=['http://localhost:3000']) 

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
    json_body = [
        {
            "measurement": "events",
            "time": get_random_time(),
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
    result = client.query(query)
    return jsonify(list(result.get_points()))