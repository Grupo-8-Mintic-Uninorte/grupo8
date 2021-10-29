from app import app
from controllers.Views import Views
from controllers.Auth import Auth
from controllers.Admin import Admin
from controllers.Student import Student
from controllers.Professor import Professor

app.add_url_rule('/', view_func=Views.index)
app.add_url_rule('/index', view_func=Views.index)

app.add_url_rule('/login', view_func=Auth.login, methods=["GET", "POST"])
app.add_url_rule('/logout', view_func=Auth.logout)
app.add_url_rule('/password/remember', view_func=Auth.remember,
                 methods=["GET", "POST"])
app.add_url_rule('/password/new/<user_id>', view_func=Auth.change,
                 methods=["GET", "POST"])


# Admin Routes
app.add_url_rule('/admin', view_func=Admin.home)


app.add_url_rule('/admin/users', view_func=Admin.users)
app.add_url_rule('/admin/users/role/<user_role>', view_func=Admin.users)
app.add_url_rule('/admin/users/<user_id>', view_func=Admin.user)
app.add_url_rule('/admin/users/new', view_func=Admin.user_new,
                 methods=["GET", "POST"])
app.add_url_rule('/admin/users/edit/<user_id>',
                 view_func=Admin.user_edit, methods=["GET", "POST"])
app.add_url_rule('/admin/users/delete/<user_id>',
                 view_func=Admin.user_delete)

app.add_url_rule('/admin/activities', view_func=Admin.activities)
app.add_url_rule('/admin/activities/<activity_id>',
                 view_func=Admin.activity)
app.add_url_rule('/admin/activities/new', view_func=Admin.activity_new)
app.add_url_rule('/admin/activities/edit/<activity_id>',
                 view_func=Admin.activity_edit, methods=["GET", "POST"])
app.add_url_rule('/admin/activities/delete/<activity_id>',
                 view_func=Admin.activity_delete)

app.add_url_rule('/admin/courses', view_func=Admin.courses)
app.add_url_rule('/admin/courses/<course_id>', view_func=Admin.course, methods=["GET", "POST"]) #
app.add_url_rule('/admin/courses/new',
                 view_func=Admin.course_new, methods=["GET", "POST"])
app.add_url_rule('/admin/courses/edit/<course_id>',
                 view_func=Admin.course_edit, methods=["GET", "POST"])
app.add_url_rule('/admin/courses/delete/<course_id>',
                 view_func=Admin.course_delete)


# Students routes
app.add_url_rule('/student', view_func=Student.home_student)
app.add_url_rule('/student/courses', view_func=Student.courses_student)
app.add_url_rule('/student/activities', view_func=Student.activities_student)
app.add_url_rule('/student/profile', view_func=Student.home_student)
app.add_url_rule('/student/profile/edit',
                 view_func=Student.home_student, methods=["GET", "POST"])


# Professor routes
app.add_url_rule('/professor', view_func=Professor.home_professor)
app.add_url_rule('/professor/students', view_func=Professor.students_professor)
app.add_url_rule('/professor/courses', view_func=Professor.courses_professor)
app.add_url_rule('/professor/activities',
                 view_func=Professor.activities_professor)
app.add_url_rule('/professor/profile', view_func=Professor.home_professor)
app.add_url_rule('/professor/profile/edit',
                 view_func=Professor.home_professor, methods=["GET", "POST"])

app.add_url_rule('/profile/user/<user_id>', view_func=Auth.profile, methods=["GET", "POST"])
