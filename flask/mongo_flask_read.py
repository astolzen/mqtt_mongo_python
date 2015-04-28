#!/bin/python
# Simple Python-Flask Script to Display all content from Mongo DB on a web page
# Requires
# - flask
# - flask-bootstrap
# - python-pymongo
# - flask.ext.pymongo
# - python-pymongo-gridfs


from flask import Flask
from flask.ext.pymongo import PyMongo
from flask import render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
app.config['MONGO_HOST'] = 'localhost'
app.config['MONGO_PORT'] = 27017
app.config['MONGO_DBNAME'] = 'test'
mongo = PyMongo(app, config_prefix='MONGO')
#mongo = PyMongo(app)

@app.route('/')
def home_page():
    mqtt_messages = mongo.db.testcol01.find()
    return render_template('mqtt.html',mqtt_messages=mqtt_messages)

if __name__ == "__main__":
    app.run(debug=True)


