from flask import Flask, render_template
from .config import Config
from .routes import home
from flask_migrate import Migrate
from .models import db, Package


app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(home.bp)
db.init_app(app)

migrate = Migrate(app, db)
