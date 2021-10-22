from flask import render_template, redirect
from controllers.Forms import LoginForm, RememberPasswordForm, ChangePassword


class Auth:

    def login():
        form = LoginForm()
        form.select.default = 1
        role = email = password = None
        if form.validate_on_submit():
            role = form.select.data
            email = form.email.data
            password = form.password.data

        form.process()
        if(role == "admin" and email == "email@gmail.com" and password == "123456789"):
            return redirect('/admin')
        else:
            form.select.default = role
            form.email.data = email
            return render_template('./pages/page_login.html', form=form)

    def logout():
        return redirect('/')

    # @requires_auth
    def remember():
        form = RememberPasswordForm()
        email = None
        if form.validate_on_submit():
            email = form.email.data

        form.process()

        if(email == "email@gmail.com"):
            return redirect("/login")
        return render_template('./pages/page_remember_password.html', form=form)

    def change():
        form = ChangePassword()
        edit_password = confirm_password = None
        if form.validate_on_submit():
            edit_password = form.edit_password.data
            confirm_password = form.confirm_password.data

        form.process()

        if(edit_password != None and confirm_password != None):
            return redirect('/admin/profile')
        else:
            return render_template('./pages/page_change_password.html', form=form)
