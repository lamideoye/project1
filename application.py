import os
import csv

from flask import Flask, session, render_template, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
    

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    books = db.execute("SELECT * FROM books LIMIT 10").fetchall()
    return render_template('index.html', books=books)

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/registered", methods=["POST"])
def registered():
    name = request.form.get("name")
    return render_template('registered.html', name=name)

@app.route("/books")
def books():
    return render_template("books.html")

@app.route("/accounts")
def accounts():
    return render_template("accounts.html")
