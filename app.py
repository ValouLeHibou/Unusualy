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


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Vos informations sont invalides, veuillez réessayer !'
        else:
            return render_template('matching.html')
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


######## PROFIL ADMIN #########
sex = "homme"
wantedsex = "osef"
region = "bretagne"
age = 29
wantedage = [18, 30]
trait = ["gentil", "mignion", "travailleur"]
traitimportant = "non"
allergy = ["eau", "soleil", "oxygene"]
allergyimportant = "oui"
###############################


@app.route('/algo')
def match():
    return algo(sex, wantedsex, region, age, wantedage, trait, traitimportant, allergy, allergyimportant)


if __name__ == '__main__':
    app.run(debug=True)

