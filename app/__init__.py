from flask import Flask, render_template
from .config import Config
from .routes import home
app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(home.bp)