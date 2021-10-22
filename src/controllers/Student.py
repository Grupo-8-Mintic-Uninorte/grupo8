from flask import render_template
from controllers.Decorators import access

from jinja_partials import render_partial

from controllers.forms import UserProfile, NewCourse, NewUser

# para generar una cadena aleatoria
import random
import string
letters = string.ascii_uppercase


class Student:
    def home_student():
        return render_template('./pages/student/student_home.html')
    def courses_student():
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
            return render_template('./pages/student/student_courses.html', table=table)
    def activities_student():
            table = {
                "titles": ['actividad', 'curso', 'codigo', 'actiones'],
                "styles": ['',          '',      '',       'd-flex justify-content-around'],
                "rows": [
                    ['actividad prediseñada', 'curso academico', 'ABC123456',
                    render_partial('./components/icon.html', plural=True, icons=['edit btn btn-success', 'eye btn btn-primary', 'trash btn btn-warning'])],
                    ['actividad prediseñada', 'curso academico', 'ABC123456',
                    render_partial('./components/icon.html', plural=True, icons=['edit btn btn-success', 'eye btn btn-primary', 'trash btn btn-warning'])],
                    ['actividad prediseñada', 'curso academico', 'ABC123456',
                    render_partial('./components/icon.html', plural=True, icons=['edit btn btn-success', 'eye btn btn-primary', 'trash btn btn-warning'])],
                    ['actividad prediseñada', 'curso academico', 'ABC123456',
                    render_partial('./components/icon.html', plural=True, icons=['edit btn btn-success', 'eye btn btn-primary', 'trash btn btn-warning'])],
                    ['actividad prediseñada', 'curso academico', 'ABC123456',
                    render_partial('./components/icon.html', plural=True, icons=['edit btn btn-success', 'eye btn btn-primary', 'trash btn btn-warning'])],
                    ['actividad prediseñada', 'curso academico', 'ABC123456',
                    render_partial('./components/icon.html', plural=True, icons=['edit btn btn-success', 'eye btn btn-primary', 'trash btn btn-warning'])],

                ]
            }
            return render_template('./pages/student/student_activities.html', table=table)
