# import necessary libraries
import os

import scrape

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


@app.route('/')
def home():
    options = scrape.option_scrape()
    cities_list = []
    data = {options,cities_list}

    return render_template('index.html',data=data)

@app.route('/scrape/<region>')
def region_scrapper(region):
    cities_list = scrape.region_scrapper(region)
    options = scrape.options_scrapper()

    data = {options,cities_list}

    return render_template('index.html',data=data)


    



if __name__ == '__main__':
    app.run(debug=True)
    