from app import app
from flask import render_template, request
import model 

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/cek', methods = ['POST', 'GET'])
def cek():
	if request.method == 'POST':
		sms = request.form['sms']
		result = model.cek(sms)
		return result