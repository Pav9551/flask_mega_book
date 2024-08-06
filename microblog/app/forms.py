from  flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FileField, HiddenField
from wtforms.validators import DataRequired
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    #photo =  FileField('filename')
    submit = SubmitField('Sign in')
class AlgebraForm(FlaskForm):
    answer = StringField('Ответ', validators=[DataRequired()])
    hidden_data = HiddenField('HiddenData')
    submit = SubmitField('Подтвердить')
