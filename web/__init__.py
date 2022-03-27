from flask import Flask, render_template

# import web.controllers
import web.config as config


app = Flask(__name__)
app.config['APP_NAME'] = config.APP_NAME


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
