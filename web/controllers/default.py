from web import app

from flask import redirect, render_template


# Home Page Display
@app.route('/')
def index():
    return render_template('home.html')


# Redirects anyone who clicks on about to my personal site
@app.route('/about')
def about():
    return redirect('https://griffinansel.com/')
