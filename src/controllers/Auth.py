from flask import render_template, redirect, url_for, flash, request, session

from controllers.Forms import LoginForm, RememberPasswordForm, ChangePassword
from controllers.Database import Database
from controllers.Secure import encrypt

db = Database('notas.db')


class Auth:

    def login():
        form = LoginForm()
        change = ChangePassword()
        form.select.default = 1
        user = None

        if form.validate_on_submit():
            user = db.readOne(
                'users', 'user_id, user_email, user_password, user_role', 'user_email="%s"' % form.email.data)

            if user is not None:
                if user[2] == '':
                    flash('El usuario no tiene contraseña asignada')
                    return redirect('/password/new/%s' % user[0])
                else:
                    validate = db.validate('users', 'user_id, user_email, user_password, user_role', [
                        ('user_role', form.select.data),
                        ('user_email', form.email.data),
                        ('user_password', encrypt(form.password.data)),
                    ])
                    print(validate)
                    if validate:
                        session.permanent = True
                        session['logged'] = True
                        session['role'] = user[3]

                        if session['role'] == 1:
                            return redirect('/admin')

                        if session['role'] == 2:
                            return redirect('/professor')

                        if session['role'] == 3:
                            return redirect('/student')

                    else:
                        flash('Usuario o contraseña incorrectos')
            else:
                flash('Usuario no encontrado')

        return render_template('./pages/page_login.html', form=form)
        form.process()

    def logout():
        session.clear()
        return redirect('/')

    # @requires_auth
    def remember():
        form = RememberPasswordForm()

        return render_template('./pages/page_remember_password.html', form=form)

    def change(user_id=None):

        form = ChangePassword()

        if user_id:
            form.user_id.default = user_id

        if form.validate_on_submit():

            user = db.readOne('users', 'user_id, user_password',
                              "user_id='%s'" % user_id)

            if len(user) > 0 and user[1] == '':

                password = encrypt(form.new_password.data)

                db.update('users', ['user_password'], [
                          password], 'user_id=%s' % user[0])

                flash('Contraseña actualizada')
                return redirect("/login")

        form.process()
        return render_template('./pages/page_change_password.html', form=form)
