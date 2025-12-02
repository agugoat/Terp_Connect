from flask import Flask, render_template
import json

with open('data/clubs.json', 'r') as file:
    data = json.load(file)

print(data)
print(type(data))


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

def clubs():
    return render_template('clubs.html')

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/search')
def search():
    clubTables = ("Name", "Category", "Contact", "Description", "Tags")

    with open('data/clubs.json') as f:
        clubData = json.load(f)

        return render_template('templates/clubs.html', clubData = clubData, clubTables = clubTables)
