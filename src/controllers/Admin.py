from flask import render_template


class Admin:
    def activities():
        return render_template('./pages/admin/admin_activities.html')

    def courses():
        return render_template('./pages/admin/admin_courses.html')

    def profile():
        return render_template('./pages/admin/admin_profile.html')
