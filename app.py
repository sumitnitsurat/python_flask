from flask import Flask
from flask_restful import Api
from resources.routes import initialize_routes
from database.db import initialize_db
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
api = Api(app)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/recipe-bag'
}

initialize_db(app)
initialize_routes(api)
app.run()