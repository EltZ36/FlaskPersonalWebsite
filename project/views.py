  
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
  
@app.route('/contact')
def contact():
    return render_template('contact.html')
  
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')
