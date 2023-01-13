from influxdb import InfluxDBClient
client = InfluxDBClient(host='0.0.0.0', port=8086, username='admin', password='password', database='test')
