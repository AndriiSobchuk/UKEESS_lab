import urllib.request
from flask import Flask, jsonify, request
from flask_sslify import SSLify

app = Flask(__name__)
sslify = SSLify(app)

@app.route('/')
def hello():
    external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    return jsonify({'message': 'Hello UKEESS', 'ip_address': external_ip})

if __name__ == '__main__':
    app.run(ssl_context=('cert.pem', 'key.pem'))

