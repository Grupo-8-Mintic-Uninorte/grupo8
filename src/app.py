import os
import jinja_partials
from flask import Flask
from controllers.Database import Database

print(Database.readOne('users', 'user_name, user_lastname', 'user_role', 3))

project_root = os.path.dirname(__file__)
template_path = os.path.join(project_root, 'templates')

app = Flask(__name__, template_folder=template_path)

app.secret_key = os.urandom(24)

jinja_partials.register_extensions(app)

import routes

if __name__ == '__main__':
    app.run()
