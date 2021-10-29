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
            validate = db.validate('users', 'user_id, user_email, user_password, user_role', [
                ('user_email', form.email.data),
                ('user_role', form.select.data)
            ])

            print(validate)

            user = db.readOne(
                'users', 'user_id, user_email, user_password, user_role', "user_email='%s'" % form.email.data)

            print(user)

            if user:
                session.permanent = True
                session['logged'] = validate
                session['role'] = user[3]

                print(session)

                if(user[2] == '' and form.email.data == user[1]):
                    return redirect('./password/new/%s' % user[0])

                if session.get('logged') and encrypt(form.password.data) == user[2]:
                    return redirect('/admin')

            elif not user:
                flash('Usuario o contraseña incorrecto')

        flash('Usuario o contraseña incorrecto')
        return render_template('./pages/page_login.html', form=form)

        form.process()


    def logout():
        session.clear()
        return redirect('/')

    # @requires_auth
    def remember():
        form=RememberPasswordForm()

        return render_template('./pages/page_remember_password.html', form=form)

    def change(user_id=None):
        form=ChangePassword()
        if user_id:
            form.user_id.default=user_id
        print(form.data)
        if form.validate_on_submit():
            user=db.readOne('users', 'user_id, user_password',
                            "user_id='%s'" % user_id)
            print(form.data)
            print(user)
            if len(user) > 0 and user[1] == '':
                password=encrypt(form.new_password.data)
                print(password)
                db.update('users', ['user_password'], [
                          password], 'user_id=%s' % user[0])
                flash('Contraseña actualizada')
                return redirect("/login")
        form.process()

        return render_template('./pages/page_change_password.html', form=form)
