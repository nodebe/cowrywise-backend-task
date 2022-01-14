from flask import Flask
from flask_restful import Api
from uuid_keys import  UKeys

app = Flask(__name__)

api = Api(app)

# endpoint to call generated_keys
api.add_resource(UKeys, '/generated_keys')


if __name__ == '__main__':
    app.run()