from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/clubs')
def clubs():
    # clubTables = ("Name", "Category", "Contact", "Description", "Tags")

    with open('data/clubs.json') as f:
        clubData = json.load(f)

    return render_template('clubs.html', clubs = clubData)

@app.route('/survey')
def survey():
    return render_template('survey.html')

@app.route('/join')
def join():
    return render_template('join.html')

if __name__ == '__main__':
    app.run(debug=True)