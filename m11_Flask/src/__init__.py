from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import config

app = Flask(__name__)
app.config.from_object(config.Config)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.debug = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from src import routes, models

