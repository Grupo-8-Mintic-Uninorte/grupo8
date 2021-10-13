from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import EmailField


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired('Campo obligatorio')], render_kw={
                       "class": "form-control", "placeholder": "Email"})
    password = PasswordField('Password', validators=[DataRequired(
        'Campo obligatorio')], render_kw={"class": "form-control", "placeholder": "Password"})
    submit = SubmitField('LOGIN', render_kw={"class": "btn btn-primary"})


class RememberPasswordForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired('Campo obligatorio')], render_kw={
                       "class": "form-control", "placeholder": "Email"})
    submit = SubmitField('Send Email', render_kw={"class": "btn btn-warning"})
