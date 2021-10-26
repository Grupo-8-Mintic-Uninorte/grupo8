import string
import random
from flask import render_template, redirect, url_for, flash, request, abort, session
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
        return render_template('./pages/admin/admin_home.html', info_cards=cards)

    # USERS
    def users(user_role="", page=""):
        if user_role == "":
            user_role = 'view_users'
            page = '/admin/users'
        elif user_role == 'professors':
            user_role = 'view_professors'
        elif user_role == 'students':
            user_role = 'view_students'
        else:
            page = '/admin/users'
            user_role == 'view_users'

        users = []
        users_database = db.readAll(user_role, "*")

        for user in users_database:
            user = list(user)
            user.append(render_partial('./components/link.html', links=[
                {
                        'route': '..%s/%d' % (page, user[0]),
                        'action': 'primary',
                        'icon': 'eye'
                        },
                {
                    'route': '..%s/edit/%d' % (page, user[0]),
                    'action': 'success',
                    'icon': 'edit'
                },
                {
                    'route': '..%s/delete/%d' % (page, user[0]),
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
        db.delete('users', "user_id=%d" % user_id)
        flash("El usuario registrado con el id %d ha sido eliminado" % user_id, 'success')
        return redirect('/admin/users')

    # ACTIVITIES
    def activities():
        activities = []
        activities_database = db.readAll('view_activities', "*")

        print(activities_database)

        for activity in activities_database:
            activity = list(activity)
            activity.append(render_partial('./components/link.html', links=[
                {
                    'route': 'activities/%d' % activity[0],
                    'action': 'primary',
                    'icon': 'eye'
                },
                {
                    'route': 'activities/edit/%d' % activity[0],
                    'action': 'success',
                    'icon': 'edit'
                },
                {
                    'route': 'activities/delete/%d' % activity[0],
                    'action': 'danger',
                    'icon': 'trash-alt'
                }
            ]
            ))
            activities.append(activity)

        table = {
            "titles": ['ID', 'ACTIVIDAD', 'DESCRIPCION', 'CURSO', 'ENTREGA', 'NOTA', 'actiones'],
            "styles": ['',          '',      '', '', '', '',       'd-flex justify-content-around'],
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
        db.delete('activities', "activity_id=%d" % activity_id)
        return redirect('/admin/activities')

    # COURSES
    def courses():
        courses = []
        courses_database = db.readAll('view_courses', '*')

        for c in courses_database:
            course = list(c)
            course.append(
                render_partial('./components/link.html', links=[
                    {
                        'route': '../admin/courses/%d' % (course[0]),
                        'action': 'primary',
                        'icon': 'eye'
                    },
                    {
                        'route': '../admin/courses/edit/%d' % (course[0]),
                        'action': 'success',
                        'icon': 'edit'
                    },
                    {
                        'route': '../admin/courses/delete/%d' % (course[0]),
                        'action': 'danger',
                        'icon': 'trash-alt'
                    },
                ])
            )
            courses.append(course)

        table = {
            "titles": ['curso', 'NOMBRE PROFESOR', 'APELLIDO PROFESOR', 'CURSO', 'HORARIO', 'ACCIONES'],
            "styles": ['visually-hidden',          '',      '','','',       'd-flex justify-content-around'],
            "rows": courses
        }
        return render_template('./pages/admin/admin_courses.html', table=table)

    def course(course_id=None):
        return 'course {}'.format(course_id)

    def course_new():
        form = NewCourse()
        form.professor_course.select = 0
        if form.validate_on_submit():
            print(form.data)

        form.process()

        return render_template('./pages/page_new_course.html', form=form)

# TODO: crear fun generadora de insert dict de formulario
    def course_edit(course_id=None):
        form = EditCourse()
        form.professor_course.select = 0
        form.validate_on_submit()
        form.process()
        return 'edit course {}'.format(course_id)

    def course_delete(course_id=None):
        db.delete('courses', "course_id=%d" % course_id)
        return redirect('/admin/courses')

    def profile():
        form = UserProfile()
        return render_template('./pages/admin/admin_profile.html', form=form)
