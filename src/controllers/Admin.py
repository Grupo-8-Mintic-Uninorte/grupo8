from flask import render_template


class Admin:
    def home():
        return render_template('./pages/admin/admin_home.html')

    #USERS
    def users():
        return render_template('./pages/admin/admin_users.html')

    def user(user_id=None):
        return 'user {0}'.format(user_id)

    def user_new():
        return 'new user'

    def user_edit(user_id=None):
        return 'edit user {}'.format(user_id)

    def user_delete(user_id=None):
        return 'delete user'

    #ACTIVITIES
    def activities():
        return render_template('./pages/admin/admin_activities.html')

    def activity(activity_id=None):
        return 'activity {}'.format(activity_id)

    def activity_new():
        return 'new activity'

    def activity_edit(activity_id=None):
        return 'edit activity {}'.format(activity_id)

    def activity_delete(activity_id=None):
        return 'delete activity {}'.format(activity_id)

    #COURSES
    def courses():
        return render_template('./pages/admin/admin_courses.html')

    def course(course_id=None):
        return 'course {}'.format(course_id)

    def course_new():
        return 'new course'

    def course_edit(course_id=None):
        return 'edit course {}'.format(course_id)

    def course_delete(course_id=None):
        return 'delete course {}'.format(course_id)

    def profile():
        return render_template('./pages/admin/admin_profile.html')
