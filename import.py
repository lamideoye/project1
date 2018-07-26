import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

#load in the csv file
#load in the csv file
def main():
    f=open("books.csv")
    reader = csv.reader(f)
    for title, author, isbn, year in reader:
        db.execute("INSERT INTO books(title, author, isbn, year) VALUES (:title, :author, :isbn, :year)",{"title":title, "author":author, "isbn":isbn, "year":year})