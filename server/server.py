from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/blood')
def page_blood():
    return render_template('hello_blood.html')


@app.route('/frost')
def page_frost():
    return render_template('hello_frost.html')


@app.route('/necr')
def page_necr():
    return render_template('hello_necr.html')


@app.route('/')
def home():
    return render_template('hello.html')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=7890)
