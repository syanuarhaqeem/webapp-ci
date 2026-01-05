from flask import Flask
import platform
import os
import psutil
from healthcheck import healthcheck

app = Flask(__name__)
app.register_blueprint(healthcheck)

@app.route("/")
def index():
    return f"""
<b>OS</b> {platform.system()} <br>
<b>CPU Usage (%)</b> {psutil.cpu_percent(interval=1)} <br>
<b>Memory Usage (%)</b> {psutil.virtual_memory().percent} <br>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
