from flask import Flask
from config import Config
from flask_cors import CORS

from .models import db
from flask_migrate import Migrate
from .api.routes import api

app = Flask(__name__)
CORS(app, origins=['*'])


app.config.from_object(Config)

app.register_blueprint(api)

db.init_app(app)
migrate = Migrate(app, db)


from . import routes
from . import models