from flask import Flask
from datetime import datetime
from database import connect
from healthcheck import healthcheck

app = Flask(__name__)
app.register_blueprint(healthcheck)

@app.route("/")
def index():
    try:
        conn = connect()
        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS access_logs (
                id SERIAL PRIMARY KEY,
                datetime TIMESTAMP
            )
        """)

        now = datetime.now()

        cur.execute(
            "INSERT INTO access_logs (datetime) VALUES (%s)",
            (now,)
        )

        conn.commit()
        cur.close()
        conn.close()

        return f"Access logged at {now}. Hello!", 200

    except Exception as e:
        return f"Error: {e}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
