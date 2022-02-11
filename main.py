from datetime import datetime
from flask import Flask, render_template, redirect

gamestate = {
    'spring_1901': {
        'Deadline': '2022-02-19', 
        'Austria': {
            'Vienna': 'A',
            'Budapest': 'A',
            'Trieste': 'F'},
        'England': {
            'London': 'F',
            'Edinburg': 'F',
            'Liverpool': 'A'},
        'France': {
            'Paris': 'A'}
    }
}

turns = {
    'spring_1901':1}                

current_turn = max(turns, key=turns.get)

utc = datetime.utcnow().replace(microsecond=0)
    
app = Flask(__name__)

@app.after_request
def add_security_headers(response):
    response.headers['X-Frame-Options']='DENY'
    response.headers['X-content-type-options']='nosniff'
    response.headers['Referrer-Policy']='no-referrer'
    response.headers['X-xss-protection']='1; mode=block; report=https://jpoirierlavoie.report-uri.com/r/d/xss/enforce'
    response.headers['Strict-Transport-Security']='max-age=31536000; includeSubDomains; preload'
    response.headers['Expect-CT']='max-age=31536000, enforce, report-uri=\"https://jpoirierlavoie.report-uri.com/r/d/ct/enforce\"'
    response.headers['Report-To']='{"group":"default","max_age":31536000,"endpoints":[{"url":"https://jpoirierlavoie.report-uri.com/a/d/g"}],"include_subdomains":true}'
    response.headers['NEL']='{"report_to":"default","max_age":31536000,"include_subdomains":true}'
    response.headers['Content-Security-Policy']='default-src \'self\'; img-src \'self\' data:; script-src-elem \'unsafe-inline\' https://cdn.jsdelivr.net; style-src-elem \'unsafe-inline\' https://cdn.jsdelivr.net; report-uri https://jpoirierlavoie.report-uri.com/r/d/csp/enforce'
    return response

@app.route('/')
def home():
    return redirect('/turn/' + current_turn, code=302)

@app.route('/about')
def about():
    return render_template('about.html', utc=utc, turns=turns, current_turn=current_turn, gamestate=gamestate)

@app.route('/turn/<turn>')
def turn(turn):
    title = turn.capitalize().replace("_", " ")
    return render_template('/turn/' + turn + '.html', title=title, turns=turns, turn=turn, utc=utc, current_turn=current_turn, gamestate=gamestate)

@app.route('/rules')
def rules():
    return render_template('rules.html', utc=utc, turns=turns, current_turn=current_turn, gamestate=gamestate)

@app.route('/orders')
def orders():
    return render_template('orders.html', utc=utc, turns=turns, current_turn=current_turn, gamestate=gamestate)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
