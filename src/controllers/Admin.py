from flask import render_template
from controllers.Decorators import access

from jinja_partials import render_partial

from controllers.Forms import UserProfile, NewCourse, NewUser, NewActivity, EditCourse

# para generar una cadena aleatoria
import random
import string
letters = string.ascii_uppercase


class Admin:
    def home():
        return render_template('./pages/admin/admin_home.html')

    # USERS
    def users():
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
        return render_template('./pages/admin/admin_users.html', table= table)

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
