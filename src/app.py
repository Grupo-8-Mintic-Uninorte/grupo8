import os
import jinja_partials

from flask import Flask

# from controllers.Database import Database

# db = Database('notas.db')

# print(db.readOne('users', "*", "user_id=2"))

# db.create(
#     'users',
#     ['user_id', 'user_role', 'user_name', 'user_lastname'],
#     [1,'Edwin', 'Marroquin']
# )

# db.update(
#     'users',
#     ['user_id', 'user_role'],
#     [5,1]
# )

# db.delete('users', 'user_id=5')

# print(db.validate(
#         "users",
#         "user_role",
#         [ ("user_email", "marrokin2@gmail.com"), ("user_password", 123456789) ] ))

# print(db.readAll('view_users','*'))

project_root = os.path.dirname(__file__)

template_path = os.path.join(project_root, 'templates')

app = Flask(__name__, template_folder=template_path)

app.secret_key = os.urandom(24)

app.debug = True

jinja_partials.register_extensions(app)

"""
    IMPORTANT:  No mover esta linea de este lugar
                Ya que las rutas deben ser leidas
                luego de inicializar la aplicacion
"""
import routes

if __name__ == '__main__':
    app.run()
