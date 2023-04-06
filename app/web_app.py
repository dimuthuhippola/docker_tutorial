from flask import Flask
from flask_restful import Api
from werkzeug.serving import WSGIRequestHandler


application = Flask(__name__)
application.secret_key = "MYSECRETKEY"


@application.route('/')
def home():
    return "Home page"


api = Api(application)

if __name__ == '__main__':
    WSGIRequestHandler.protocol_version = "HTTP/1.1"
    application.run(host="0.0.0.0", debug=True, port=5000)
