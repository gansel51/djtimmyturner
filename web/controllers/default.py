from web import app

from flask import render_template


# Display the home page
@app.route('/about')
@app.route('/')
def index():
    return render_template('home.html')