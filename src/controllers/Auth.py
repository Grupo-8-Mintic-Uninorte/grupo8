from flask import render_template, redirect, url_for, flash, request, session
from controllers.Forms import LoginForm, RememberPasswordForm, ChangePassword
from controllers.Database import Database

db = Database('notas.db')

class Auth:

    def login():
        form = LoginForm()
        form.select.default = 1
        user = None

        if form.validate_on_submit():
            print(form.data)
            user = db.validate('users', 'user_role', [
                ('user_email', form.email.data),
                ('user_password', form.password.data),
                ('user_role', form.select.data)
            ])
            if user:
                session['logged'] = user
                session['role'] = form.select.data
                print(session)
                return redirect('/admin')
            elif not user:
                flash('Usuario o contraseña incorrecto')

        return render_template('./pages/page_login.html', form=form)

        form.process()

    def logout():
        session.clear()
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
