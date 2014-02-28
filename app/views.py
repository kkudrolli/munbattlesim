from flask import render_template, request
from app import app

@app.route('/')
@app.route('/index', methods=['GET','POST'])
def index():
    return render_template("index.html")

@app.route('/test', methods=['GET','POST'])
def print_form():
    if request.method == 'POST':
        return render_template('form.html',result=request.form['fooput'])
    if request.method == 'GET':
        return render_template('form.html')

