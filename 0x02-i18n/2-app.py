#!/usr/bin/env python3
""" flask application"""

from flask import Flask, render_template, request
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)


class Config:
    """Represents flask Babel configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """return the best match from the supported
    languages based on the request"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def get_index() -> str:
    """welcome to flask application"""
    title = gettext("Welcome to Holberton")
    return render_template('2-index.html', title=title)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
