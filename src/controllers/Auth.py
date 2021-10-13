from flask import render_template, redirect
from controllers.Forms import LoginForm, RememberPasswordForm


class Auth:
    def login():
        form = LoginForm()
        return render_template('./pages/page_login.html', form=form)

    def logout():
        return redirect('/')

    # @requires_auth
    def remember():
        form = RememberPasswordForm()
        return render_template('./pages/page_remember_password.html', form=form)

    def submit():
        form = LoginForm()
        if form.validate_on_submit():
            return redirect('/example')
