from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, BooleanField, StringField
from wtforms.validators import ValidationError, DataRequired, InputRequired, Length, EqualTo, Email
from wtforms.fields import SelectField
from wtforms.fields.html5 import DateField, EmailField


class LoginForm(FlaskForm):
    select = SelectField(
        label=('User Role'),
        choices=[
            ("", "Select a role"),
            ("admin", "Administrator"),
            ("professor", "Professors"),
            ("student", "Student")
        ],
        validators=[InputRequired("debe escoger una opcion")]
    )
    email = StringField(
        label=('Email'),
        validators=[
            DataRequired('correo electronico requerido'),
            Length(max=120, message='no puede ser mayor a %(max)d caracteres')
        ]
    )
    password = PasswordField(
        label=('Password'),
        validators=[
            DataRequired('contraseña obligatoria'),
            Length(min=8, message='la contraseña debe tener minimo %(min)d caracteres'),
            Length(max=32, message='la contraseña debe tener maximo %(max)d caracteres')
        ]
    )
    submit = SubmitField(label=('ACCESS TO PLATFORM'))


class RememberPasswordForm(FlaskForm):
    email = EmailField(
        label=('Email'),
        validators=[
            Email('Email no valido'),
            InputRequired('no ha ingresado un email'),
            Length(max=120, message="no puede ser mayor a %(max)d caracteres")
        ]
    )
    submit = SubmitField(label=('Send Email'))


class UserProfile(FlaskForm):
    name = StringField(
        label=('Nombre(s)'),
        validators=[
            DataRequired('El campo nombre es requerido')
        ]
    )
    last_name = StringField(
        label=('Apellido(s)'),
        validators=[
            DataRequired('El campo apellido es requerido')
        ]
    )
    date = DateField(
        label=('Fecha de nacimiento'),
        format='%Y-%m-%d',
        validators=[
            DataRequired('El campo nombre es requerido')
        ]
    )

    edit_profile = SubmitField(
        label=('Actualizar informacion')
    )


class ChangePassword(FlaskForm):
    edit_password = PasswordField(
        label=('Password'),
        validators=[
            DataRequired('contraseña obligatoria'),
            EqualTo('confirm_password',
                    message="las contraseñas deben ser iguales"),
            Length(min=8, message='la contraseña debe tener minimo %(min)d caracteres'),
            Length(max=32, message='la contraseña debe tener maximo %(max)d caracteres')
        ]
    )
    confirm_password = PasswordField(
        label=('Confirm Password'),
        validators=[
            DataRequired('no ha confirmado la contraseña')
        ]
    )
    submit = SubmitField(label=('Update password'))
