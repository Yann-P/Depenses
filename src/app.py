#! /usr/bin/python3.4

"""
    Depenses
    Software to share a budget in a group.

    :copyright: (c) 2017 by Yann Pellegrini.
    :license: GPLv3, see LICENSE for more details.
"""

from datetime import datetime
from flask import Flask, request, session, url_for, redirect, \
     render_template, abort, g
from flask_script import Manager, Server
from controllers.user import user


app = Flask('depenses')

manager = Manager(app)

app.register_blueprint(user, url_prefix='/user')

app.config.from_object('app')


@app.route('/')
def index():
    return ""

server = Server(host="127.0.0.1", port="8080")
manager.add_command("server", server)

if __name__ == '__main__':
    manager.run()
