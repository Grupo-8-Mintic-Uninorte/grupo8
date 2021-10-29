import string
import random
from datetime import datetime
from flask import render_template, redirect, url_for, flash, request, abort, session
from controllers.Decorators import Autorize

from jinja_partials import render_partial

from controllers.Forms import UserProfile, NewCourse, NewUser, NewActivity, EditCourse

from controllers.Database import Database

db = Database('notas.db')

class Admin:
    @Autorize.login
    @Autorize.is_admin
    def home():
        print(session)
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
    @Autorize.login
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
                    'route': '../../profile/user/%d' % user[0],
                    'action': 'primary',
                    'icon': 'eye'
                },
                {
                    'route': '..%s/delete/%d' % (page, user[0]),
                    'action': 'danger',
                    'icon': 'delete'
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

    @Autorize.login
    def user(user_id=None):
        return render_template('./pages/page_user.html', id=user_id)

    @Autorize.login
    def user_new():
        form = NewUser()
        if form.validate_on_submit():

            # Campos que deben ser eliminados
            clean_fields = [
                'confirm_password',
                'submit',
                'csrf_token'
            ]

            #encriptacion del password
            form.user_password.data = ''

            # Convertir el formulario en listas
            keys = list(form.data.keys())
            values = list(form.data.values())

            # Eliminar los campos que no se deben enviar
            for c in clean_fields:
                i = keys.index(c)
                values.pop(i)
                keys.remove(c)

            try:
                # Insertar el usuario en la base de datos
                db.create('users', keys, values)
                flash("El usuario ha sido registrado con exito", 'success')
            except:
                flash("Error en la consulta", 'error')
            return redirect('/admin/users')
        form.process()
        return render_template('./pages/page_user_new.html', form=form)

    @Autorize.login
    def user_edit(user_id):
        user_database = db.readOne('users', "*", "user_id=%d" % user_id)
        form = NewUser()

        form.user_id.default = user_database[0]
        form.user_name.default = user_database[2]
        form.user_lastname.default = user_database[3]
        form.user_dateborn.default = datetime.strptime(user_database[4], '%Y-%m-%d').date()
        form.user_email.default = user_database[5]
        form.user_phone.default = user_database[6]
        form.user_active.default = user_database[8]
        if form.validate_on_submit():
            # db.update('users', form.data.keys(), form.data.values(), "user_id=%d" % user_id, )
            db.create('users', form.data.keys(), form.data.values(), "user_id=%d" % form.user_id.data, )
            flash("El usuario registrado con el id %d ha sido editado" % user_id, 'success')
            return redirect('/admin/users')
        form.process()
        return render_template('./pages/page_user_edit.html', form=form)

    @Autorize.login
    def user_delete(user_id=None):
        db.delete('users', "user_id=%d" % user_id)
        flash("El usuario registrado con el id %d ha sido eliminado" % user_id, 'error')
        return redirect('/admin/users')

    # ACTIVITIES
    @Autorize.login
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
                    'icon': 'pencil'
                },
                {
                    'route': 'activities/delete/%d' % activity[0],
                    'action': 'danger',
                    'icon': 'delete'
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

    @Autorize.login
    def activity(activity_id=None):
        return 'activity {}'.format(activity_id)

    @Autorize.login
    def activity_new():
        form = NewActivity()
        if form.validate_on_submit():
            clean_fields = [
                'submit',
                'csrf_token'
            ]
            # Convertir el formulario en listas
            keys = list(form.data.keys())
            values = list(form.data.values())

            # Eliminar los campos que no se deben enviar
            for c in clean_fields:
                i = keys.index(c)
                values.pop(i)
                keys.remove(c)

            try:
                # Insertar el usuario en la base de datos
                db.create('activities', keys, values)
                flash("La actividad ha sido registrada con exito", 'success')
            except:
                flash("Error en la consulta", 'error')
            return redirect('/admin/activities')
        form.process()
        return render_template('./pages/page_new_admin_activity.html', form=form)

    @Autorize.login
    def activity_edit(activity_id=None):
        return 'edit activity {}'.format(activity_id)

    def activity_delete(activity_id=None):
        db.delete('activities', "activity_id=%d" % activity_id)
        flash("La actividad registrada con el id %d ha sido eliminado" % activity_id, 'error')
        return redirect('/admin/activities')

    # COURSES
    @Autorize.login
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
                        'icon': 'pencil'
                    },
                    {
                        'route': '../admin/courses/delete/%d' % (course[0]),
                        'action': 'danger',
                        'icon': 'delete'
                    },
                ])
            )
            courses.append(course)

        table = {
            "titles": ['curso', 'NOMBRE PROFESOR', 'APELLIDO PROFESOR', 'CURSO', 'HORARIO', 'ACCIONES'],
            "styles": ['visually-hidden',          '',      '','','',       'd-flex justify-content-around'],
            "count_courses": len(courses),
            "rows": courses
        }
        return render_template('./pages/admin/admin_courses.html', table=table)

    def course(course_id):
        c = db.readOne('courses', '*', "course_id=%s" % course_id)
        info_course= {
            "   ": c[1],
        }
        print(info_course)
        return render_template('./pages/page_course.html', course=info_course)

    @Autorize.login
    def course_new():
        form = NewCourse()
        if form.validate_on_submit():
            clean_fields = [
                'submit',
                'csrf_token'
            ]
            keys = list(form.data.keys())
            values = list(form.data.values())
            for c in clean_fields:
                i = keys.index(c)
                values.pop(i)
                keys.remove(c)
            try:
                print(values)
                db.create('courses', keys, values)
                flash("El curso ha sido registrado con exito", 'success')
            except:
                flash("Error en la consulta", 'error')
            return redirect('/admin/courses')
        form.process()

        return render_template('./pages/page_course_new.html', form=form)
# TODO: crear fun generadora de insert dict de formulario

    @Autorize.login
    def course_edit(course_id):
        course = db.readOne('courses', "*","course_id=%s" % course_id)
        professors = db.readAll('view_professors', '*')

        professor_default = [(i, '%s %s' % (p[2], p[3])) for i,p in enumerate(professors) if p[0] == course[1]]

        form = EditCourse()

        form.course_id.default = course[0]
        form.course_name.default = course[2]
        form.course_professor.default = professor_default[0][0]
        form.course_description.default = course[3]
        form.course_schedule.default = datetime.strptime(
            course[4], '%Y-%m-%d')
        form.course_limit.default = course[5]

        if form.validate_on_submit():
            print(form.data.keys())
            print(form.data.values())

        form.process()

        return render_template('./pages/page_course_edit.html', form=form)

    def course_delete(course_id):
        db.delete('courses', "course_id=%d" % course_id)
        flash("El curso registrado con el id %d ha sido eliminado" % course_id, 'error')
        return redirect('/admin/courses')

