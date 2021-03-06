from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import PasswordField, SubmitField, BooleanField, StringField, HiddenField
from wtforms.validators import ValidationError, DataRequired, InputRequired, Length, EqualTo, Email
from wtforms.fields import SelectField, IntegerField, FileField
from wtforms.fields.html5 import DateField, EmailField, TelField
from wtforms.widgets import TextArea

from controllers.Database import Database
from controllers.Secure import decrypt, encrypt

db = Database('notas.db')

choises_profile = [(i, p) for i, p in db.readAll('roles', '*')]
choises_profile.insert(0, ('', 'Seleccione un perfil'))


class LoginForm(FlaskForm):
    select = SelectField(
        label=('User Role'),
        choices=choises_profile,
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
    user_id = HiddenField()
    old_password = PasswordField(
        label=('Old Password'),
        validators=[
            Length(max=32, message='la contraseña debe tener maximo %(max)d caracteres')
        ]
    )
    new_password = PasswordField(
        label=('New Password'),
        validators=[
            DataRequired('Ingrese la nueva contraseña'),
            Length(min=8, message='la contraseña debe tener minimo %(min)d caracteres'),
            Length(max=32, message='la contraseña debe tener maximo %(max)d caracteres')
        ]
    )
    submit = SubmitField(label=('Update password'))


class EditCourse(FlaskForm):
    professors = []
    professors_database = db.readAll(
        'view_professors', 'user_name, user_lastname')
    professors = list(professors_database)

    professors = [(index, '%s %s' % (name[0], name[1]))
                  for index, name in enumerate(professors)]
    professors.insert(0, ('0', 'Seleccione un profesor'))

    course_id = HiddenField(
        default=len(professors_database) + 1
    )

    course_name = StringField(
        label=("Nombre Curso"),
        validators=[
            DataRequired("El curso debe tener nombre"),
            Length(max=120, message="El titulo debe contener máximo %(min)d caracteres")
        ]
    )

    course_professor = SelectField(
        label=("Escoja un profesor"),
        choices=professors,
        validators=[InputRequired("debe escoger una opcion")]
    )

    course_description = StringField(
        label=("Descripcion del curso"),
        validators=[
            DataRequired("La descripcion del curso es obligatoria"),
            Length(
                max=200, message="La descripcion debe contener maximo %(max)d caracteres"),
        ],
        widget=TextArea()
    )

    course_schedule = DateField(
        label=('Fecha de inicio'),
        validators=[
            InputRequired("Se require la fecha de inicio del curso")
        ],
        format='%Y-%m-%d'
    )

    course_limit = IntegerField(
        label=("Número de estudiantes"),
        validators=[
            DataRequired("Se require el numero de estudiantes edecuado")
        ]
    )

    submit = SubmitField(label=('Create a course'))


class NewCourse(FlaskForm):
    professors = []
    professors_database = db.readAll(
        'view_professors', 'user_name, user_lastname')
    professors = list(professors_database)

    professors = [(index, '%s %s' % (name[0], name[1]))
                  for index, name in enumerate(professors)]

    professors.insert(0, ('0', 'Seleccione un profesor'))

    course_id = HiddenField(
        default=len(professors_database) + 1
    )

    course_name = StringField(
        label=("Nombre Curso"),
        validators=[
            DataRequired("El curso debe tener nombre"),
            Length(max=120, message="El titulo debe contener máximo %(min)d caracteres")
        ]
    )

    course_professor = SelectField(
        label=("Escoja un profesor"),
        choices=professors,
        validators=[InputRequired("debe escoger una opcion")]
    )

    course_description = StringField(
        label=("Descripcion del curso"),
        validators=[
            DataRequired("La descripcion del curso es obligatoria"),
            Length(
                max=200, message="La descripcion debe contener maximo %(max)d caracteres"),
        ],
        widget=TextArea()
    )

    course_schedule = DateField(
        label=('Fecha de inicio'),
        validators=[
            DataRequired("Se require la fecha de inicio del curso")
        ],
        format='%Y-%m-%d'
    )

    course_limit = IntegerField(
        label=("Número de estudiantes"),
        validators=[
            DataRequired("Se require el numero de estudiantes edecuado")
        ]
    )
    submit = SubmitField(label=('Create a course'))


class NewUser(FlaskForm):
    user_id = HiddenField(
        default=len(db.readAll('users', 'user_id')) + 1
    )

    user_role = SelectField(
        label=('User Role'),
        choices=choises_profile,
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
        format='%Y-%m-%d'
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

    user_password = PasswordField()
    confirm_password = PasswordField()

    user_active = BooleanField("Usuario activo", false_values = (False, 'false', 0, '0'))

    submit = SubmitField("Registrar nuevo usuario")


class NewActivity(FlaskForm):
    courses = []
    courses_database = db.readAll(
        'courses', 'course_name')
    courses = list(courses_database)

    courses = [(index, '%s' % name[0])
               for index, name in enumerate(courses)]

    courses.insert(0, ('0', 'Seleccione un curso'))

    activity_id = HiddenField(
        default=len(courses_database) + 1
    )

    activity_course = SelectField(
        label=('Curso'),
        choices=courses,
        validators=[InputRequired("debe escoger una opcion")]
    )
    activity_name = StringField(
        label=("Nombre Actividad"),
        validators=[
            DataRequired("La actividad debe tener nombre"),
            Length(min=20, message="El titulo debe contener mínimo %(min)d caracteres"),
            Length(max=120, message="El titulo debe contener máximo %(min)d caracteres")
        ]
    )

    activity_description = StringField(
        label=("Descripcion de la actividad"),
        validators=[
            DataRequired("La descripcion del curso es obligatoria"),
            Length(
                min=20, message="La descripcion debe contener mínimo %(min)d caracteres"),
            Length(
                max=200, message="La descripcion debe contener maximo %(max)d caracteres"),
        ],
        widget=TextArea()
    )
    activity_note = IntegerField(
        label=("Nota máxima a alcanzar"),
        validators=[
            DataRequired("Se require la nota máxima a alcanzar")
        ]
    )
    activity_deadline = DateField(
        label=('Fecha de inicio'),
        validators=[
            DataRequired("Se require la fecha de finalización de la actividad")
        ],
        format='%Y-%m-%d'
    )

    submit = SubmitField(label=('Create an activity'))
