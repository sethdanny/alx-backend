#!/usr/bin/env python3
"""
Route module for translation/time zone normalizing application
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
app = Flask(__name__)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """gets user dictionary from user table based on url param"""
    user_id = request.args.get('login_as')
    if user_id:
        user_id = int(user_id)
    return users.get(user_id)


class Config():
    """babel configuration"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """determine best match with supported languages"""
    locale = request.args.get('locale')
    if locale and locale in Config.LANGUAGES:
        return locale
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.before_request
def before_request():
    """sets user as global variable"""
    g.user = get_user()


@app.route('/')
def index():
    """renders html template"""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
