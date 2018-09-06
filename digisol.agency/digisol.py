from flask import Flask, render_template, url_for, flash, redirect, request
from forms import ContactForm
from flask_mail import Message, Mail
from secrets import mail_login, mail_password, slack_api_token
from slacker import Slacker

app = Flask(__name__)
app.secret_key = 'kQXNNq+bIj2v>H|~,=!Y2Sd&=QbbG0'
app.debug = True

# emailing stuff
app.config.update(dict(
    MAIL_SERVER = 'smtp.googlemail.com',
    MAIL_PORT = 465,
    MAIL_USE_TLS = False,
    MAIL_USE_SSL = True,
	# change these values to your email account, or set them in secrets.py
    MAIL_USERNAME = mail_login,
    MAIL_PASSWORD = mail_password
))

mail = Mail(app)

# Slack messages
slackClient = Slacker(slack_api_token)


@app.route('/', methods=['GET', 'POST'])
def index():
	form = ContactForm()
	# check user's browser languages
	langz = request.accept_languages
	rusish = langz.find('ru')
	ukrainish = langz.find('uk')

	if request.method == 'POST':
		msg = Message('Topic with email: example@cock.ua', sender='marzique@gmail.com', recipients=['admin@digisol.agency'])
		msg.body = """
		      From: %s <%s>
		      %s
		      """ % (form.name.data, form.email.data, form.message.data)
		mail.send(msg)
		slackClient.chat.post_message('#forms_digisol', '*[New message]* --- from <*' + form.email.data + '*>'
									  + '    *content*:   ' + form.message.data)

		return redirect(url_for('index'))

	elif request.method == 'GET':
		if rusish >= 0:
			if ukrainish >= 0:
				print(langz)
				return render_template('index_ua.html', form=form)
			else:
				print(langz)
				return render_template('index_ru.html', form=form)
		elif ukrainish >= 0:
			print(langz)
			return render_template('index_ua.html', form=form)
		else:
			print(langz)
			return render_template('index_en.html', form=form)

# google verification
@app.route('/google0e58ce55dc995c8c.html')
def google():
	return render_template('google0e58ce55dc995c8c.html')

if __name__ == '__main__':
	app.run()

