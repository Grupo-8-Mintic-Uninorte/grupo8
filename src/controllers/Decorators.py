from flask import redirect, request, session, flash
from functools import wraps


class Autorize:

    def login(f):
        @wraps(f)
        def wrap(*args, **kwargs):
            if 'logged' in session:
                return f(*args, **kwargs)
            else:
                flash('Acceso no autorizado')
                return redirect('/login')
        return wrap

    def is_admin(f):
        @wraps(f)
        def wrap(*args, **kwargs):
            if session['role'] == '1':
                return f(*args, **kwargs)
            else:
                flash('Acceso no autorizado')
                return redirect('/login')
        return wrap

    def is_professor(f):
        @wraps(f)
        def wrap(*args, **kwargs):
            if session['role'] == '2':
                return f(*args, **kwargs)
            else:
                flash('Acceso no autorizado')
                return redirect('/login')
        return wrap

    def is_student(f):
        @wraps(f)
        def wrap(*args, **kwargs):
            if session['role'] == '3':
                return f(*args, **kwargs)
            else:
                flash('Acceso no autorizado')
                return redirect('/login')
        return wrap
