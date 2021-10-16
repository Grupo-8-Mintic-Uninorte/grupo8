from flask import render_template
from controllers.Decorators import access

from jinja_partials import render_partial

from controllers.Forms import UserProfile

# para generar una cadena aleatoria
import random
import string
letters = string.ascii_uppercase


class Admin:
    def home():
        return render_template('./pages/admin/admin_home.html')

    # USERS
    def users():
        return render_template('./pages/admin/admin_users.html')

    def user(user_id=None):
        return render_template('./pages/page_user.html', id=user_id)

    def user_new():
        return 'new user'

    def user_edit(user_id=None):
        return 'edit user {}'.format(user_id)

    def user_delete(user_id=None):
        return 'delete user'

    # ACTIVITIES
    def activities():
        table = {
            "titles": ['', 'actividad', 'curso', 'codigo', 'actiones'],
            "styles": ['', '',          '',      '',       'd-flex justify-content-around'],
            "rows": [
                [render_partial('./components/icon.html', plural=False, icons='home'), 'actividad prediseñada', 'curso academico', 'ABC123456',
                 render_partial('./components/icon.html', plural=True, icons=['edit btn btn-success', 'eye btn btn-primary', 'trash btn btn-warning'])],
                [render_partial('./components/icon.html', plural=False, icons='home'), 'actividad prediseñada', 'curso academico', 'ABC123456',
                 render_partial('./components/icon.html', plural=True, icons=['edit btn btn-success', 'eye btn btn-primary', 'trash btn btn-warning'])],
                [render_partial('./components/icon.html', plural=False, icons='home'), 'actividad prediseñada', 'curso academico', 'ABC123456',
                 render_partial('./components/icon.html', plural=True, icons=['edit btn btn-success', 'eye btn btn-primary', 'trash btn btn-warning'])],
                [render_partial('./components/icon.html', plural=False, icons='home'), 'actividad prediseñada', 'curso academico', 'ABC123456',
                 render_partial('./components/icon.html', plural=True, icons=['edit btn btn-success', 'eye btn btn-primary', 'trash btn btn-warning'])],
                [render_partial('./components/icon.html', plural=False, icons='home'), 'actividad prediseñada', 'curso academico', 'ABC123456',
                 render_partial('./components/icon.html', plural=True, icons=['edit btn btn-success', 'eye btn btn-primary', 'trash btn btn-warning'])],
                [render_partial('./components/icon.html', plural=False, icons='home'), 'actividad prediseñada', 'curso academico', 'ABC123456',
                 render_partial('./components/icon.html', plural=True, icons=['edit btn btn-success', 'eye btn btn-primary', 'trash btn btn-warning'])],
                [render_partial('./components/icon.html', plural=False, icons='home'), 'actividad prediseñada', 'curso academico', 'ABC123456',
                 render_partial('./components/icon.html', plural=True, icons=['edit btn btn-success', 'eye btn btn-primary', 'trash btn btn-warning'])],
                [render_partial('./components/icon.html', plural=False, icons='home'), 'actividad prediseñada', 'curso academico', 'ABC123456',
                 render_partial('./components/icon.html', plural=True, icons=['edit btn btn-success', 'eye btn btn-primary', 'trash btn btn-warning'])],
                [render_partial('./components/icon.html', plural=False, icons='home'), 'actividad prediseñada', 'curso academico', 'ABC123456',
                 render_partial('./components/icon.html', plural=True, icons=['edit btn btn-success', 'eye btn btn-primary', 'trash btn btn-warning'])],
                [render_partial('./components/icon.html', plural=False, icons='home'), 'actividad prediseñada', 'curso academico', 'ABC123456',
                 render_partial('./components/icon.html', plural=True, icons=['edit btn btn-success', 'eye btn btn-primary', 'trash btn btn-warning'])],
            ]
        }
        return render_template('./pages/admin/admin_activities.html', table=table)

    def activity(activity_id=None):
        return 'activity {}'.format(activity_id)

    def activity_new():
        return 'new activity'

    def activity_edit(activity_id=None):
        return 'edit activity {}'.format(activity_id)

    def activity_delete(activity_id=None):
        return 'delete activity {}'.format(activity_id)

    # COURSES
    def courses():
        table = {
            "titles": ['', 'curso', 'profesor', 'codigo', 'actiones'],
            "styles": ['', '',          '',      '',       'd-flex justify-content-around'],
            "rows": [
                [render_partial('./components/icon.html', plural=False, icons='home'), 'actividad prediseñada', 'curso academico', 'ABC123456',
                 render_partial('./components/icon.html', plural=True, icons=['edit btn btn-success', 'eye btn btn-primary', 'trash btn btn-warning'])],
                [render_partial('./components/icon.html', plural=False, icons='home'), 'actividad prediseñada', 'curso academico', 'ABC123456',
                 render_partial('./components/icon.html', plural=True, icons=['edit btn btn-success', 'eye btn btn-primary', 'trash btn btn-warning'])],
                [render_partial('./components/icon.html', plural=False, icons='home'), 'actividad prediseñada', 'curso academico', 'ABC123456',
                 render_partial('./components/icon.html', plural=True, icons=['edit btn btn-success', 'eye btn btn-primary', 'trash btn btn-warning'])],
                [render_partial('./components/icon.html', plural=False, icons='home'), 'actividad prediseñada', 'curso academico', 'ABC123456',
                 render_partial('./components/icon.html', plural=True, icons=['edit btn btn-success', 'eye btn btn-primary', 'trash btn btn-warning'])],
                [render_partial('./components/icon.html', plural=False, icons='home'), 'actividad prediseñada', 'curso academico', 'ABC123456',
                 render_partial('./components/icon.html', plural=True, icons=['edit btn btn-success', 'eye btn btn-primary', 'trash btn btn-warning'])],
                [render_partial('./components/icon.html', plural=False, icons='home'), 'actividad prediseñada', 'curso academico', 'ABC123456',
                 render_partial('./components/icon.html', plural=True, icons=['edit btn btn-success', 'eye btn btn-primary', 'trash btn btn-warning'])],
                [render_partial('./components/icon.html', plural=False, icons='home'), 'actividad prediseñada', 'curso academico', 'ABC123456',
                 render_partial('./components/icon.html', plural=True, icons=['edit btn btn-success', 'eye btn btn-primary', 'trash btn btn-warning'])],
                [render_partial('./components/icon.html', plural=False, icons='home'), 'actividad prediseñada', 'curso academico', 'ABC123456',
                 render_partial('./components/icon.html', plural=True, icons=['edit btn btn-success', 'eye btn btn-primary', 'trash btn btn-warning'])],
                [render_partial('./components/icon.html', plural=False, icons='home'), 'actividad prediseñada', 'curso academico', 'ABC123456',
                 render_partial('./components/icon.html', plural=True, icons=['edit btn btn-success', 'eye btn btn-primary', 'trash btn btn-warning'])],
                [render_partial('./components/icon.html', plural=False, icons='home'), 'actividad prediseñada', 'curso academico', 'ABC123456',
                 render_partial('./components/icon.html', plural=True, icons=['edit btn btn-success', 'eye btn btn-primary', 'trash btn btn-warning'])]
            ]
        }
        return render_template('./pages/admin/admin_courses.html', table = table)

    def course(course_id=None):
        return 'course {}'.format(course_id)

    def course_new():
        return 'new course'

    def course_edit(course_id=None):
        return 'edit course {}'.format(course_id)

    def course_delete(course_id=None):
        return 'delete course {}'.format(course_id)

    def profile():
        form = UserProfile()
        return render_template('./pages/admin/admin_profile.html', form=form)
