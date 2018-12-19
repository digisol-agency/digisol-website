from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, InputRequired
from wtforms.fields.html5 import EmailField

class ContactForm(FlaskForm):
	name = StringField('Ім&#39я користувача',
						   validators=[DataRequired(), Length(min=2, max=20)])
	email = EmailField('Email',
						validators=[InputRequired(), Email('please input valid email')])
	message = TextAreaField('Повідомлення', validators=[DataRequired()])

	submit = SubmitField('Отправить')
