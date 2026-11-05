
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Database connection
def get_db():
    conn = sqlite3.connect("home.db")
    return conn

# HOME PAGE
@app.route('/')
def index():
    return render_template("index.html")


# LIGHT 1 CONTROL
@app.route('/light1/<status>')
def light1(status):
    status = status.upper()

    if status not in ["ON", "OFF"]:
        return "Invalid status", 400

    with get_db() as conn:
        conn.execute(
            "UPDATE devices SET light1=? WHERE id=1",
            (status,)
        )

    return render_template("index.html", msg="Light1 is " + status)


# LIGHT 2 CONTROL
@app.route('/light2/<status>')
def light2(status):
    status = status.upper()

    if status not in ["ON", "OFF"]:
        return "Invalid status", 400

    with get_db() as conn:
        conn.execute(
            "UPDATE devices SET light2=? WHERE id=1",
            (status,)
        )

    return render_template("index.html", msg="Light2 is " + status)


# CHECK LIGHT STATUS
@app.route('/check_status')
def check_status():
    with get_db() as conn:
        cur = conn.execute(
            "SELECT light1, light2 FROM devices WHERE id=1"
        )
        row = cur.fetchone()

    if row is None:
        return "Device not found", 404

    return str(row[0]) + "," + str(row[1])


# RUN APPLICATION
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
