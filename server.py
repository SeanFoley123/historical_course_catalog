import os, atexit

import pandas as pd
from flask import Flask, redirect, render_template, request, url_for

import retrieveData as retrieve
import storeData as store

import sqlite3

sqlite_file = "data.sqlite"

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

app = Flask(__name__)

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

@app.route('/new_user')
def new_user_page():	
    return render_template('new_user.html')

@app.route('/new_user', methods=['POST'])
def new_user():	
	name = request.form['name']
	username = request.form['username']
	store.new_student(c, name, username)
	return redirect("/login")

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

def end_func(conn):
	conn.commit()
	conn.close()

if __name__ == '__main__':
	atexit.register(end_func, conn=conn)
	app.run(debug=True, threaded=True)