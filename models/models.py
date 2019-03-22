# models.py

from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    genre = db.Column(db.String(1000))
    firstname = db.Column(db.String(1000))
    lastname = db.Column(db.String(1000))
    age = db.Column(db.Integer)
    email = db.Column(db.String(100))
    loc = db.Column(db.String(50))
    caract = db.Column(db.String(1000))
    hobby = db.Column(db.String(1000))
    dscr = db.Column(db.String(1000))
    al1 = db.Column(db.String(1000))
    al2 = db.Column(db.String(1000))
    al3 = db.Column(db.String(1000))
    al4 = db.Column(db.String(1000))
    al5 = db.Column(db.String(1000))
    caract1 = db.Column(db.String(1000))
    caract2 = db.Column(db.String(1000))
    caract3 = db.Column(db.String(1000))
    password = db.Column(db.String(1000))

    def __init__(self, genre, firstname, lastname, age, email, loc, caract, hobby, dscr, al1, al2, al3, al4, al5, caract1, caract2, caract3, password):
        self.genre = genre
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.email = email
        self.loc = loc
        self.caract = caract
        self.hobby = hobby
        self.dscr = dscr
        self.al1 = al1
        self.al2 = al2
        self.al3 = al3
        self.al4 = al4
        self.al5 = al5
        self.caract1 = caract1
        self.caract2 = caract2
        self.caract3 = caract3
        self.password = password
