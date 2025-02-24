from flask import render_template, Flask


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandex_lyceum_secret_key'

@app.route('/<title>')
@app.route('/index<title>')
def index(title):
    return render_template("base.html", title=title)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
