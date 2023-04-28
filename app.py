from flask import Flask, render_template
from flask_ngrok import run_with_ngrok

app = Flask(__name__, static_url_path='/static')
run_with_ngrok(app)

@app.route('/')
def index():
    return render_template('index.html')

if __name__== '__main__':
    app.run()
