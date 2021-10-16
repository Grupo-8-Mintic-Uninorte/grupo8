from app import app
from controllers.Views import Views
from controllers.Auth import Auth
from controllers.Admin import Admin

app.add_url_rule('/', view_func=Views.index)
app.add_url_rule('/index', view_func=Views.index)
app.add_url_rule('/example', view_func=Views.example)

app.add_url_rule('/login', view_func=Auth.login, methods=["GET", "POST"])
app.add_url_rule('/logout', view_func=Auth.logout)
app.add_url_rule('/submit', view_func=Auth.submit)
app.add_url_rule('/password/remember', view_func=Auth.remember, methods=["GET", "POST"])
app.add_url_rule('/password/change', view_func=Auth.change, methods=["GET", "POST"])


# Admin Routes
app.add_url_rule('/admin', view_func=Admin.home)

app.add_url_rule('/admin/users', view_func=Admin.users)
app.add_url_rule('/admin/user/<int:user_id>', view_func=Admin.user)
app.add_url_rule('/admin/users/new', view_func=Admin.user_new)
app.add_url_rule('/admin/users/edit/<int:user_id>', view_func=Admin.user_edit)
app.add_url_rule('/admin/users/delete/<int:user_id>', view_func=Admin.user_delete)

app.add_url_rule('/admin/activities', view_func=Admin.activities)
app.add_url_rule('/admin/activity/<int:activity_id>', view_func=Admin.activity)
app.add_url_rule('/admin/activities/new', view_func=Admin.activity_new)
app.add_url_rule('/admin/activities/edit/<int:activity_id>', view_func=Admin.activity_edit)
app.add_url_rule('/admin/activities/delete/<int:activity_id>', view_func=Admin.activity_delete)

app.add_url_rule('/admin/courses', view_func=Admin.courses)
app.add_url_rule('/admin/course/<int:course_id>', view_func=Admin.course)
app.add_url_rule('/admin/courses/new', view_func=Admin.course_new)
app.add_url_rule('/admin/courses/edit/<int:course_id>', view_func=Admin.course_edit)
app.add_url_rule('/admin/courses/delete/<int:course_id>', view_func=Admin.course_delete)


app.add_url_rule('/admin/profile', view_func=Admin.profile)
