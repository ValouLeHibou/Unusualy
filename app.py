from flask import Flask, render_template, redirect, url_for, request, session
from matching import algo

app = Flask(__name__)
app.debug = True

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
            error = 'Invalides informations. Veuillez réessayer !'
            session['logged_in'] = False
        else:
            return redirect('/')
            session['logged_in'] = True
    return render_template('login.html', error=error)


@app.route('/inscription', methods=['GET', 'POST'])
def inscription():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('inscription.html', error=error)


@app.route('/algo')
def match():
    return render_template("algo.html", algo=algo(sex, wantedsex, region, age, wantedage, trait, traitimportant, allergy, allergyimportant))


if __name__ == '__main__':
    app.run(debug=True)

