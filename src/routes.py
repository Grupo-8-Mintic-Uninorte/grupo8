from app import app
from controllers.Views import Views
from controllers.Auth import Auth

app.add_url_rule('/', view_func=Views.index)
app.add_url_rule('/index', view_func=Views.index)
app.add_url_rule('/example', view_func=Views.example)

app.add_url_rule('/login', view_func=Auth.login)
app.add_url_rule('/remember', view_func=Auth.remember)
app.add_url_rule('/submit', view_func=Auth.submit)
