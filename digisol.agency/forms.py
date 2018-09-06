from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, InputRequired


class ContactForm(FlaskForm):
	name = StringField('Ім&#39я користувача',
						   validators=[DataRequired(), Length(min=2, max=20)])
	email = StringField('Email',
						validators=[InputRequired(), Email('please input valid email')])
	message = TextAreaField('Повідомлення', validators=[DataRequired()])

	submit = SubmitField('Отправить')
