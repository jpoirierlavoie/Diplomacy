from datetime import datetime
from flask import Flask, render_template

players = {
    'Austria': 'Test', 
    'England': 'TBD',
    'France': 'TBD',
    'Germany': 'TBD',
    'Italy': 'TBD',
    'Russia': 'TBD',
    'Turkey': 'TBD'}
turns = {
    1: 'spring_1901',
    2: 'fall_1901'}
    
app = Flask(__name__)
app.wsgi_app = wrap_wsgi_app(app.wsgi_app)

@app.route('/home')
@app.route('/')
def home():
    return render_template('home.html', title="Home", players=players, turns=turns)

@app.route('/turn/<turn>')
def turn(turn):
    title = turn.capitalize().replace("_", " ")
    utc=datetime.utcnow().replace(microsecond=0)
    return render_template('/turn/' + turn + '.html', title=title, utc=utc, turn=turn, turns=turns, players=players)

@app.route('/orders')
def orders():
    return render_template('orders.html', title="Orders")

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
