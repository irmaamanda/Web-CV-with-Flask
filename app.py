from flask import Flask, render_template
from flask_ngrok import run_with_ngrok

app = Flask(_name_, static_url_path='/static')
run_with_ngrok(app)

@app.route('/')
def index():
    return render_template('index.html')

if _name== 'main_':
    app.run()