import json
import os
from datetime import datetime
from pprint import pprint

#from braintree import NotFoundError

from flask import Flask, Response
from flask import flash, jsonify, render_template, request, redirect, url_for, make_response

from flask_mailman import EmailMessage, Mail

import flask_wtf

from flask_security import SQLAlchemySessionUserDatastore, Security, login_required, auth_required, roles_accepted, roles_required, current_user
from flask_security.forms import LoginForm
from flask_security.utils import login_user
from flask_security.views import after_this_request

from dotenv import load_dotenv
from werkzeug.utils import secure_filename

from database import db
from db import DB
from models.auth import User, Role

import braintree
 
app = Flask(__name__,
            static_url_path='/static',
            static_folder='static')

UPLOAD_FOLDER = './static/uploads'
# ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

## CONFIG ##################################################
app.config['TEMPLATES_AUTO_RELOAD'] = True

app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECURITY_REGISTERABLE"] = True
