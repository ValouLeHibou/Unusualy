# main.py

from flask import Flask, render_template, request, session
from models import db
from models.models import User
from matching import algo

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///workshopdb.sqlite3'

with app.app_context():
    db.init_app(app)
    db.create_all()
sex = "homme"
wantedsex = "femme"
region = "bretagne"
age = 30
wantedage = [18, 30]
trait = ["gentil", "social", "travailleur"]
traitimportant = "non"
allergy = ["eau", "soleil", "oxygene"]
allergyimportant = "oui"


femme = [
    "femme"
    "homme",
    "Paris",
    100,
    25,
    [18, 29],
    ["insupportable", "social", "flemmarde", "serviable"],
    "oui",
    ["eau", "soleil", "oxygene"],
    "oui"
]


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    session['logged_in'] = False
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Vos informations sont invalides, veuillez réessayer !'
            #session['logged_in'] = False
        else:
            return render_template('index.html')
            #session['logged_in'] = True
    return render_template('login.html', error=error)


@app.route('/inscription')
def inscription():
    return render_template('inscription.html')


@app.route('/matching', methods = ['POST', 'GET'])
def matching():
    if request.method == 'POST':
       user = User(
            request.form.get("genre"),
            request.form.get("firstname"),
            request.form.get("lastname"),
            request.form.get("age"),
            request.form.get("email"),
            request.form.get("loc"),
            request.form.get("caract"),
            request.form.get("hobby"),
            request.form.get("descr"),
            request.form.get("al1"),
            request.form.get("al2"),
            request.form.get("al3"),
            request.form.get("al4"),
            request.form.get("al5"),
            request.form.get("caract1"),
            request.form.get("caract2"),
            request.form.get("caract3"),
            request.form.get("password")
       )
       print(user)
       db.session.add(user)
       db.session.commit()
       matching = User.query.all()
       return render_template("matching.html", matching=matching)
    else:
        result = User.query.all()
        return render_template("matching.html", matching=result)


app.run(port=8080, debug=True)
@app.route('/algo')
def match():
    return render_template("algo.html", algo=algo(sex, wantedsex, region, age, wantedage, trait, traitimportant, allergy, allergyimportant))


if __name__ == '__main__':
    app.run(debug=True)

