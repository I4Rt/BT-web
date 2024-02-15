from flask import Flask, request, json

app = Flask(__name__, static_url_path='', static_folder='frontend/static', template_folder='frontend/templates')

