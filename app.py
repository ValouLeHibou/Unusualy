from flask import Flask
from flask import render_template


app = Flask(__name__)
app.debug = True


@app.route('/<name>')
def index(name=None):
    return render_template('index.html', name=name)


@app.route('/contact/')
def contact():
    mail = "jean@bon.fr"
    tel = "01 23 45 67 89"
    return "<h1>Mail: {} --- Tel: {}</h1>".format(mail, tel)


if __name__ == '__main__':
    app.run()
