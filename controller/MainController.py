from config import *
from flask import render_template

@app.route('/main')
def getMain():
    return render_template('main.html')
