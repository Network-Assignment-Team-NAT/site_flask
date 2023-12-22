from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    return render_template('hello.html',
                           message=f"Hello, World! It is an awesome site on Flask, that you can reach from our ISP.")


@app.route('/survey', methods=['GET'])
def survey():
    return render_template('survey.html')


@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    age = request.form['age']
    country = request.form['country']
    return render_template('submit.html', message=f"Hi, {name}! I dare say you are {age} years old and from {country}!")  # use new html file, like we use in hello function. View all variables from this request


if __name__ == '__main__':
    app.run(debug=True)
import sys
print(sys.path)
