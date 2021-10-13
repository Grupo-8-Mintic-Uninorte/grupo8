from app import app
from controllers.Views import Views
from controllers.Auth import Auth
from controllers.Admin import Admin

app.add_url_rule('/', view_func=Views.index)
app.add_url_rule('/index', view_func=Views.index)
app.add_url_rule('/example', view_func=Views.example)

app.add_url_rule('/login', view_func=Auth.login)
app.add_url_rule('/remember', view_func=Auth.remember)
app.add_url_rule('/submit', view_func=Auth.submit)

app.add_url_rule('/admin', view_func=Admin.index)

app.add_url_rule('/admin/users', view_func=Admin.users)
app.add_url_rule('/admin/users/<int:user_id>', view_func=Admin.user())
app.add_url_rule('/admin/users/new', view_func=Admin.user_new())
app.add_url_rule('/admin/users/edit/<int:user_id>', view_func=Admin.user_edit())
app.add_url_rule('/admin/users/delete/<int:user_id>', view_func=Admin.user_delete())

app.add_url_rule('/admin/activities', view_func=Admin.activities)
app.add_url_rule('/admin/activities/<int:activity_id>', view_func=Admin.activity())
app.add_url_rule('/admin/activities/new', view_func=Admin.activity_new())
app.add_url_rule('/admin/activities/edit/<int:activity_id>', view_func=Admin.activity_edit())
app.add_url_rule('/admin/activities/delete/<int:activity_id>', view_func=Admin.activity_delete())

app.add_url_rule('/admin/courses', view_func=Admin.courses)
app.add_url_rule('/admin/courses/<int:course_id>', view_func=Admin.course())
app.add_url_rule('/admin/courses/new', view_func=Admin.course_new())
app.add_url_rule('/admin/courses/edit/<int:course_id>', view_func=Admin.course_edit())
app.add_url_rule('/admin/courses/delete/<int:course_id>', view_func=Admin.course_delete())


app.add_url_rule('/admin/profile', view_func=Admin.profile)
