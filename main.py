from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.after_request
def add_security_headers(response):
    response.headers['X-Frame-Options']='DENY'
    response.headers['X-content-type-options']='nosniff'
    response.headers['Referrer-Policy']='no-referrer'
    response.headers['Permissions-Policy']='geolocation=(), microphone=()'
    response.headers['X-xss-protection']='1; mode=block; report=https://jpoirierlavoie.report-uri.com/r/d/xss/enforce'
    response.headers['Strict-Transport-Security']='max-age=31536000; includeSubDomains; preload'
    response.headers['Expect-CT']='max-age=31536000, enforce, report-uri=\"https://jpoirierlavoie.report-uri.com/r/d/ct/enforce\"'
    response.headers['Report-To']='{"group":"default","max_age":31536000,"endpoints":[{"url":"https://jpoirierlavoie.report-uri.com/a/d/g"}],"include_subdomains":true}'
    response.headers['NEL']='{"report_to":"default","max_age":31536000,"include_subdomains":true}'
    response.headers['Content-Security-Policy']='default-src \'none\'; frame-src \'self\' www.google.com; connect-src \'self\' www.gstatic.com www.google.com stats.g.doubleclick.net www.google-analytics.com northamerica-northeast1-jpoirierlavoie-ca.cloudfunctions.net www.googletagmanager.com; img-src www.google-analytics.com www.google.ca www.google.com \'self\'; script-src-elem \'unsafe-inline\' www.gstatic.com www.google.com www.google-analytics.com www.googletagmanager.com \'self\'; style-src-elem \'unsafe-inline\' \'self\'; font-src \'self\'; manifest-src \'self\'; worker-src \'self\'; report-uri https://jpoirierlavoie.report-uri.com/r/d/csp/enforce'
    return response

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
