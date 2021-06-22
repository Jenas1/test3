from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo


# 문자열인지 패스워드,제출 버튼인지 원하는 폼을 지정할 수 있고 validators 통해서 길이, 필수값 ,이메일 , 유효성 검사를 할 수 있따.

class RegistrationForm(FlaskForm):
    username = StringField('아이디', validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField('이메일', validators=[DataRequired(), Email()])
    password = PasswordField('비밀번호', validators=[DataRequired(), Length(min=4, max=20)])
    confirm_password = PasswordField('비밀번호 확인', validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('가입')
