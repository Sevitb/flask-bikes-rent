from flask import Flask
from flask_mail import Mail, Message
app = Flask(__name__, template_folder='templates')
app.config.from_pyfile('config.py')

mail = Mail(app)

from . import views