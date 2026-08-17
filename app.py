from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)


def get_db_connection():
    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

    return connection


@app.route("/")
def home():
    connection = get_db_connection()

    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users ORDER BY id DESC")

    users = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template("index.html", users=users)


@app.route("/add-user", methods=["POST"])
def add_user():

    name = request.form["name"]
    email = request.form["email"]

    connection = get_db_connection()

    cursor = connection.cursor()

    query = "INSERT INTO users (name, email) VALUES (%s, %s)"

    values = (name, email)

    cursor.execute(query, values)

    connection.commit()

    cursor.close()
    connection.close()

    return redirect(url_for("home"))


@app.route("/test-db")
def test_db():

    try:
        connection = get_db_connection()

        cursor = connection.cursor()

        cursor.execute("SELECT 1")

        result = cursor.fetchone()

        cursor.close()
        connection.close()

        return f"Database connection successful: {result[0]}"

    except Exception as e:

        return f"Database connection failed: {e}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)