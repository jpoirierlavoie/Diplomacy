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
    'spring_1901':1}
    
app = Flask(__name__)

@app.route('/home')
@app.route('/')
def home():
    current_turn=max(turns, key=turns.get)
    return render_template('home.html', title="Home", players=players, turns=turns, current_turn=current_turn)

@app.route('/turn/<turn>')
def turn(turn):
    title = turn.capitalize().replace("_", " ")
    utc=datetime.utcnow().replace(microsecond=0)
    current_turn=max(turns, key=turns.get)
    return render_template('/turn/' + turn + '.html', title=title, players=players, turns=turns, turn=turn, utc=utc, current_turn=current_turn)

@app.route('/orders')
def orders():
    return render_template('orders.html', title="Orders")

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
