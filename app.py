from flask import Flask, render_template, redirect, url_for, make_response

app = Flask(__name__)

@app.route('/')
def home():
    # Redirect to the login page
    return redirect(url_for('login'))

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/sitemap.xml')
def sitemap():
    response = make_response(render_template('sitemap.xml'))
    response.headers['Content-Type'] = 'application/xml'
    return response

@app.route('/robots.txt')
def robots():
    response = make_response(render_template('robots.txt'))
    response.headers['Content-Type'] = 'text/plain'
    return response

# Redirect any unknown route to /login
@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(port=5001)
