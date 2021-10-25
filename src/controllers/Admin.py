import string
import random
from flask import render_template
from controllers.Decorators import access

from jinja_partials import render_partial

from controllers.Forms import UserProfile, NewCourse, NewUser, NewActivity, EditCourse

from controllers.Database import Database

db = Database('notas.db')

class Admin:
    def home():
        cards = {
            'actividades': 0,
            'cursos': 0,
            'profesores': 0,
            'estudiantes': 0,

        }
        cards['actividades'] = db.readOne('count_activities', '*')[0]
        cards['cursos'] = db.readOne('count_courses', '*')[0]
        cards['profesores'] = db.readOne('count_professors', '*')[0]
        cards['estudiantes'] = db.readOne('count_students', '*')[0]
        print(cards)
        return render_template('./pages/admin/admin_home.html', info_cards=cards)

    # USERS
    def users(user_role=""):
        if user_role == "":
            user_role = 'view_users'
        elif user_role == 'professors':
            user_role = 'view_professors'
        elif user_role == 'students':
            user_role = 'view_students'
        else:
            user_role == 'view_users'

        users = []
        users_database= db.readAll(user_role, "*")

        for user in users_database:
            user = list(user)
            user.append(render_partial('./components/link.html', links=[
                    {
                        'route': 'user/%d' % user[0],
                        'action': 'primary',
                        'icon': 'eye'
                    },
                    {
                        'route': 'user/edit/%d' % user[0],
                        'action': 'success',
                        'icon': 'edit'
                    },
                    {
                        'route': 'user/delete/%d' % user[0],
                        'action': 'danger',
                        'icon': 'trash-alt'
                    }
                ]
            ))
            users.append(user)

        table = {
            "titles": ['ID', 'PERFIL', 'APELLIDOS', 'NOMBRE', 'CORREO ELECTRONICO', 'actiones'],
            "styles": ['', '',          '',      '', '',       'h-100 d-flex align-items-center justify-content-around'],

            "count_students": len(list(filter(lambda x: x[1] == 'ESTUDIANTE', users))),
            "count_professors": len(list(filter(lambda x: x[1] == 'PROFESOR', users))),

            "rows": users
        }

        print(table)
        return render_template('./pages/admin/admin_users.html', table=table)

    def user(user_id=None):
        return render_template('./pages/page_user.html', id=user_id)

    def user_new():
        form = NewUser()
        form.user_role.default = "0"
        form.validate_on_submit()
        form.process()
        return render_template('./pages/page_new_user.html', form=form)

    def user_edit(user_id=None):
        return 'edit user {}'.format(user_id)

    def user_delete(user_id=None):
        return 'delete user'

    # ACTIVITIES
    def activities():
        activities = []
        activities_database = db.readAll('view_activities', "*")

        for activity in activities_database:
            activity = list(activity)
            activity.append(render_partial('./components/link.html', links=[
                {
                        'route': 'activity/%d' % activity[0],
                        'action': 'primary',
                        'icon': 'eye'
                        },
                {
                    'route': 'activity/edit/%d' % activity[0],
                    'action': 'success',
                    'icon': 'edit'
                },
                {
                    'route': 'activity/delete/%d' % activity[0],
                    'action': 'danger',
                    'icon': 'trash-alt'
                }
            ]
            ))
            activities.append(activity)

        table = {
            "titles": ['ID','ACTIVIDAD', 'DESCRIPCION', 'CURSO', 'ENTREGA','NOTA','actiones'],
            "styles": ['',          '',      '','','','',       'd-flex justify-content-around'],
            "rows": activities,
            "count_activities": len(activities)
        }
        return render_template('./pages/admin/admin_activities.html', table=table)

    def activity(activity_id=None):
        return 'activity {}'.format(activity_id)

    def activity_new():
        form = NewActivity()
        form.validate_on_submit()
        form.process()
        return render_template('./pages/page_new_admin_activity.html', form=form)

    def activity_edit(activity_id=None):
        return 'edit activity {}'.format(activity_id)

    def activity_delete(activity_id=None):
        return 'delete activity {}'.format(activity_id)

    # COURSES
    def courses():
        table = {
            "titles": ['curso', 'profesor', 'codigo', 'actiones'],
            "styles": ['',          '',      '',       'd-flex justify-content-around'],
            "rows": [
                ['curso entrenido', 'curso academico', 'ABC123456',
                 render_partial('./components/icon.html', plural=True, icons=['edit btn btn-success', 'eye btn btn-primary', 'trash btn btn-warning'])],
                ['curso entrenido', 'curso academico', 'ABC123456',
                 render_partial('./components/icon.html', plural=True, icons=['edit btn btn-success', 'eye btn btn-primary', 'trash btn btn-warning'])],
                ['curso entrenido', 'curso academico', 'ABC123456',
                 render_partial('./components/icon.html', plural=True, icons=['edit btn btn-success', 'eye btn btn-primary', 'trash btn btn-warning'])],
                ['curso entrenido', 'curso academico', 'ABC123456',
                 render_partial('./components/icon.html', plural=True, icons=['edit btn btn-success', 'eye btn btn-primary', 'trash btn btn-warning'])],
                ['curso entrenido', 'curso academico', 'ABC123456',
                 render_partial('./components/icon.html', plural=True, icons=['edit btn btn-success', 'eye btn btn-primary', 'trash btn btn-warning'])],
                ['curso entrenido', 'curso academico', 'ABC123456',
                 render_partial('./components/icon.html', plural=True, icons=['edit btn btn-success', 'eye btn btn-primary', 'trash btn btn-warning'])]
            ]
        }
        return render_template('./pages/admin/admin_courses.html', table=table)

    def course(course_id=None):
        return 'course {}'.format(course_id)

    def course_new():
        form = NewCourse()
        form.professor_course.default = "0"
        form.validate_on_submit()
        form.process()
        return render_template('./pages/page_new_course.html', form=form)

    def course_edit(course_id=None):
        form = EditCourse()
        form.professor_course.default = "0"
        form.validate_on_submit()
        form.process()
        return 'edit course {}'.format(course_id)

    def course_delete(course_id=None):
        return 'delete course {}'.format(course_id)

    def profile():
        form = UserProfile()
        return render_template('./pages/admin/admin_profile.html', form=form)
