#!/usr/bin/python3
"""
Starts a flask application that lists all states
"""

from flask import Flask, render_template
from models.state import State
from models import storage

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def get_states():
    """displays HTML oreded statesdds dssddsdsdsdssdds"""
    states = sorted(list(storage.all(State).values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown hgshdghjsjkgdhjgshdghjgsj"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
