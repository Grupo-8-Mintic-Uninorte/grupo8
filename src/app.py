import os
import jinja_partials
from flask import Flask
from controllers.Database import Database

db = Database('notas.db')

# print(db.readOne('users', "*", "user_id=2"))

# db.create(
#     'users',
#     ['user_id', 'user_role', 'user_name', 'user_lastname'],
#     [1,'Edwin', 'Marroquin']
# )

# db.update(
#     'users',
#     ['user_role'],
#     [2],
#     "user_id=5"
# )

# db.delete('users', 'user_id=5')

print(db.readAll('users', "*"))

project_root = os.path.dirname(__file__)
template_path = os.path.join(project_root, 'templates')

app = Flask(__name__, template_folder=template_path)

app.secret_key = os.urandom(24)

jinja_partials.register_extensions(app)

import routes

if __name__ == '__main__':
    app.run()
