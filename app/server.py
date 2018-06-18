#!/usr/bin/env python
import os
from flask import Flask
from flask_cors import CORS

# initialization
server = Flask(__name__)
server.config.from_object('config')

cors = CORS(server, resources={r"/api/*": {"origins": "*"}})
# import APIs
# from app.user import views
