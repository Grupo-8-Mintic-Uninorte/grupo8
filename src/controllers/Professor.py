from flask import render_template
from controllers.Decorators import Autorize

from jinja_partials import render_partial

from controllers.Forms import UserProfile, NewCourse, NewUser

# para generar una cadena aleatoria
import random
import string
letters = string.ascii_uppercase


class Professor:
    def home_professor():
        return render_template('./pages/professor/professor_home.html')
    def courses_professor():
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
                return render_template('./pages/professor/professor_courses.html', table=table)
    def activities_professor():
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
                return render_template('./pages/professor/professor_activities.html', table=table)
    def students_professor():
        table = {
            "titles": ['foto','apellidos', 'nombres', 'codigo', 'actiones'],
            "styles": ['','',          '',      '',       'h-100 d-flex align-items-center justify-content-around'],
            "rows": [
                [render_partial('./components/component_image.html', avatar=True, image="https://t3.ftcdn.net/jpg/02/33/46/24/360_F_233462402_Fx1yke4ng4GA8TJikJZoiATrkncvW6Ib.jpg", user_name="estudiante_anonimo_abc123456"),'apellido 1 apellido 2', 'nombre estudiante', 'ABC123456',
                 render_partial('./components/icon.html', plural=True, icons=['edit btn btn-success', 'eye btn btn-primary', 'trash btn btn-warning'])],
                [render_partial('./components/component_image.html', avatar=True, image="https://t3.ftcdn.net/jpg/02/33/46/24/360_F_233462402_Fx1yke4ng4GA8TJikJZoiATrkncvW6Ib.jpg", user_name="estudiante_anonimo_abc123456"),'apellido 1 apellido 2', 'nombre estudiante', 'ABC123456',
                 render_partial('./components/icon.html', plural=True, icons=['edit btn btn-success', 'eye btn btn-primary', 'trash btn btn-warning'])],
                [render_partial('./components/component_image.html', avatar=True, image="https://t3.ftcdn.net/jpg/02/33/46/24/360_F_233462402_Fx1yke4ng4GA8TJikJZoiATrkncvW6Ib.jpg", user_name="estudiante_anonimo_abc123456"),'apellido 1 apellido 2', 'nombre estudiante', 'ABC123456',
                 render_partial('./components/icon.html', plural=True, icons=['edit btn btn-success', 'eye btn btn-primary', 'trash btn btn-warning'])],
                [render_partial('./components/component_image.html', avatar=True, image="https://t3.ftcdn.net/jpg/02/33/46/24/360_F_233462402_Fx1yke4ng4GA8TJikJZoiATrkncvW6Ib.jpg", user_name="estudiante_anonimo_abc123456"),'apellido 1 apellido 2', 'nombre estudiante', 'ABC123456',
                 render_partial('./components/icon.html', plural=True, icons=['edit btn btn-success', 'eye btn btn-primary', 'trash btn btn-warning'])],
                [render_partial('./components/component_image.html', avatar=True, image="https://t3.ftcdn.net/jpg/02/33/46/24/360_F_233462402_Fx1yke4ng4GA8TJikJZoiATrkncvW6Ib.jpg", user_name="estudiante_anonimo_abc123456"),'apellido 1 apellido 2', 'nombre estudiante', 'ABC123456',
                 render_partial('./components/icon.html', plural=True, icons=['edit btn btn-success', 'eye btn btn-primary', 'trash btn btn-warning'])],
            ]
        }
        return render_template('./pages/professor/professor_students.html', table= table)
