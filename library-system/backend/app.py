from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

CORS(app)
db = SQLAlchemy(app)
jwt = JWTManager(app)

@app.route('/')
def index():
    return {
        'message': 'Library Information System API'
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
