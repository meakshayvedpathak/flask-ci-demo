from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Feature Branch!"

@app.route("/health")
def health():
    return {"status": "ok"}
