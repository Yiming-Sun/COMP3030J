from flask import render_template, flash, redirect, url_for, session
from blogapp import app

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html', title='Home')

@app.route('/sign_in')
def sign_in():
	return render_template('sign_in.html', title='Home')

@app.route('/sign_up')
def sign_up():
	return render_template('sign_up.html', title='Home')