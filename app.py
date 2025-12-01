from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

def clubs():
    return render_template('clubs.html')

if __name__ == '__main__':
    app.run(debug=True)
