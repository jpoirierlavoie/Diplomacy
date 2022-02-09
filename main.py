from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/turn/<turn>')
def turn(turn):
    return render_template("/turn/" + turn + ".html")

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
