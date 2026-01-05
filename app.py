from flask import Flask
from healthcheck import healthcheck

app = Flask(__name__)
app.register_blueprint(healthcheck)

@app.route("/")
def index():
    return "Hello world!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
