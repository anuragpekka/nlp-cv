from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/<nameahh>')
def home(nameahh):
    return redirect(url_for('index', user=nameahh))
@app.route('/hello/<user>')
def index(user):
    return render_template('hello_world.html', name=user)

if __name__ == '__main__':
    app.run(debug=True, port=5001)