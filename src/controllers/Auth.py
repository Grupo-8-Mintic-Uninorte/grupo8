from flask import render_template, redirect, url_for, flash, request, session

from datetime import datetime

from controllers.Forms import LoginForm, RememberPasswordForm, ChangePassword, NewUser
from controllers.Database import Database
from controllers.Secure import encrypt
from controllers.Decorators import Autorize

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

                    if validate:
                        session.permanent = True
                        session['logged'] = True
                        session['role'] = user[3]
                        session['id'] = user[0]

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

    @Autorize.login
    def logout():
        session.clear()
        return redirect('/')

    @Autorize.login
    def remember():
        form = RememberPasswordForm()

        return render_template('./pages/page_remember_password.html', form=form)

    @Autorize.login
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

    @Autorize.login
    def profile(user_id):

        form = NewUser()
        user = db.readOne('users', '*', 'user_id=%s' % user_id)
        roles = db.readAll('roles', '*')

        role_default = [(i, r[0]) for i, r in enumerate(roles) if r[0] == user[1]]

        print(user[8])
        print(form.user_active)

        form.user_id.default = user[0]
        form.user_role.default = role_default[0][1]
        form.user_name.default = user[2]
        form.user_lastname.default = user[3]
        form.user_dateborn.default = datetime.strptime(user[4], '%Y-%m-%d')
        form.user_email.default = user[5]
        form.user_phone.default = user[6]
        form.user_active.checked = user[8]

        if form.validate_on_submit():
            clean_fields = [
                'submit',
                'csrf_token',
                'user_password',
                'confirm_password'
                ]

            keys = list(form.data.keys())
            values = list(form.data.values())

            for c in clean_fields:
                i = keys.index(c)
                values.pop(i)
                keys.remove(c)

            try:
                db.update('users', keys, values, 'user_id=%s' % user_id)
                flash('Usuario actualizado')
                return redirect('/profile/user/%s' % user_id)
            except:
                flash('Error al actualizar')

        form.process()
        return render_template('./pages/page_user_profile.html', form=form, user=user, roles=roles)
