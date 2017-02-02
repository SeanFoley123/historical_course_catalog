"""
A Flask server that presents a minimal browsable interface for the Olin course catalog.
author: Oliver Steele <oliver.steele@olin.edu>
date  : 2017-01-18
license: MIT
"""

import os

import pandas as pd
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

# courses = pd.read_csv('./data/olin-courses-16-17.csv')

@app.route('/health')
def health():
    return 'ok'

@app.route('/')
def home_redir():
	return redirect("/login")

@app.route('/login')
def login_page():	
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():	
    username = request.form['username']
    return redirect('/user='+username)

@app.route('/user=<username>')
def your_classes(username):	
    return render_template('your_classes_home.html', username=username)

@app.route('/user=<username>/class=<class_name>')
def show_single_class(username, class_name):	
    return render_template('projects_by_class.html')

# @app.route('/project_page')
# def login():	
#     return render_template('project_page.html')

# @app.route('/input_form')
# def login():	
#     return render_template('input_form.html')

# @app.route('/area/<course_area>')
# def area_page(course_area):
#     return render_template('course_area.html', courses=courses[courses.course_area == course_area].iterrows())

if __name__ == '__main__':
	app.run(debug=True, threaded=True)