import os
import jinja_partials
from flask import Flask, request, abort
# import views

project_root = os.path.dirname(__file__)
template_path = os.path.join(project_root, 'templates')

app = Flask(__name__, template_folder=template_path)

app.secret_key = os.urandom(24)

import routes

jinja_partials.register_extensions(app)

if __name__ == '__main__':
    app.run()