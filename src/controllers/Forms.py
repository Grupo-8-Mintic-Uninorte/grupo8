from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import PasswordField, SubmitField, BooleanField, StringField
from wtforms.validators import ValidationError, DataRequired, InputRequired, Length, EqualTo, Email
from wtforms.fields import SelectField, IntegerField, FileField
from wtforms.fields.html5 import DateField, EmailField, TelField
from wtforms.widgets import TextArea


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


class NewCourse(FlaskForm):
    name_course = StringField(
        label=("Nombre Curso"),
        validators=[
            DataRequired("El curso debe tener nombre"),
            Length(min=20, message="El titulo debe contener mínimo %(min)d caracteres"),
            Length(max=120, message="El titulo debe contener máximo %(min)d caracteres")
        ]
    )

    professor_course = SelectField(
        label=("Escoja un profesor"),
        choices=[
            ("0", "Select a professor"),
            ("1", "Professor 1"),
            ("2", "Professor 2"),
            ("3", "Professor 3"),
            ("4", "Professor 4"),
        ],
        validators=[InputRequired("debe escoger una opcion")]
    )

    description_course = StringField(
        label=("Descripcion del curso"),
        validators=[
            DataRequired("La descripcion del curso es obligatoria"),
            Length(
                min=20, message="La descripcion debe contener mínimo %(min)d caracteres"),
            Length(
                max=200, message="La descripcion debe contener maximo %(max)d caracteres"),
        ],
        widget=TextArea()
    )

    schedule_course = DateField(
        label=('Fecha de inicio'),
        validators=[
            DataRequired("Se require la fecha de inicio del curso")
        ],
        format='%Y/%m/%d'
    )

    max_students_course = IntegerField(
        label=("Número de estudiantes"),
        validators=[
            DataRequired("Se require el numero de estudiantes edecuado")
        ]
    )
    submit = SubmitField(label=('Create a course'))


class NewUser(FlaskForm):
    user_photo = FileField(
			label=("Agregar foto"),
			validators=[
				FileRequired("Imagen requerida"),
				FileAllowed(
					['jpg', 'png'], 'Solo imagenes! jpg, png'
				)
			]
		)
    user_role = SelectField(
        label=('User Role'),
        choices=[
            ("", "Select a role"),
            ("admin", "Administrator"),
            ("professor", "Professors"),
            ("student", "Student")
        ],
        validators=[InputRequired("debe escoger una opcion")]
    )
    user_name = StringField(
        label=("Nombre(s)"),
        validators=[
            DataRequired("Nombre(s) de usuario requerido")
        ]
    )
    user_lastname = StringField(
        label=("Apellido(s)"),
        validators=[
            DataRequired("Apellido(s) de usuario requerido")
        ]
    )
    user_dateborn = DateField(
        label=('Fecha de nacimiento'),
        validators=[
            DataRequired("Se require la fecha de inicio del usuario")
        ],
        format='%Y/%m/%d'
    )
    user_address = StringField(
        label=("Direccion"),
        validators=[
            DataRequired("Direccion de usuario requerido")
        ]
    )
    user_email = EmailField(
        label=('Email'),
        validators=[
            Email('Email no valido'),
            InputRequired('no ha ingresado un email'),
            Length(max=120, message="no puede ser mayor a %(max)d caracteres")
        ]
    )
    user_phone = TelField(
        label=('Telefono'),
        validators=[
            DataRequired("Numero de telefono requerido")
        ]
    )

    user_active = BooleanField("Usuario activo")

    submit = SubmitField("Registrar nuevo usuario")
