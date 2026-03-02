from flask import Flask
import os

app = Flask(__name__)

# Read environment variable
ENVIRONMENT = os.getenv('ENVIRONMENT', 'local')

@app.route('/')
def home():
    return f"Hello from my CI/CD pipeline! 🚀 You are on: {ENVIRONMENT} environment 🌍"

@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    return {"result": a + b}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)