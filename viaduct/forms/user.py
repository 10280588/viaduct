from flask.ext.wtf import Form, TextField, PasswordField, BooleanField, \
		RecaptchaField, SelectField, FieldList, FormField, SubmitField
from flask.ext.wtf import Required, Email, EqualTo, IntegerField
from flask.ext.wtf import ValidationError

class SignUpForm(Form):
	email = TextField('E-mail adres', validators=[Required(message='Geen emailadres opgegeven'), Email(message='Ongelding emailadres opgegeven')])
	password = PasswordField('Wachtwoord', validators=[Required(message='Geen wachtwoord opgegeven')])
	repeat_password = PasswordField('Herhaal wachtwoord', validators=[Required(message='Wachtwoorden komen niet overeen'), EqualTo('password', message='Wachtwoorden komen niet overeen')])
	first_name = TextField('Voornaam', validators=[Required(message='Geen voornaam opgegeven')])
	last_name = TextField('Achternaam', validators=[Required(message='Geen achternaam opgegeven')])
	student_id = TextField('Studentnummer', validators=[Required(message='Geen studentnummer opgegeven')])
	education_id = SelectField('Opleiding', coerce=int)
	recaptcha = RecaptchaField()

class EditUserForm(Form):
	""" Edit a user as administrator """
	id = IntegerField('ID')
	email = TextField('E-mail adres', validators=[Required(message='Geen emailadres opgegeven'), Email(message='Ongeldig emailadres opgegeven')])
	password = PasswordField('Wachtwoord')
	repeat_password = PasswordField('Herhaal wachtwoord')
	first_name = TextField('Voornaam', validators=[Required(message='Geen voornaam opgegeven')])
	last_name = TextField('Achternaam', validators=[Required(message='Geen achternaam opgegeven')])
	has_payed = BooleanField('Heeft betaald')
	student_id = TextField('Studentnummer', validators=[Required(message='Geen studentnummer opgegeven')])
	education_id = SelectField('Opleiding', coerce=int)

	def validate_password(form, field):
		"""Providing a password is only required when creating a new user."""
		if form.id.data == 0 and len(field.data) == 0:
			raise ValidationError('Geen wachtwoord opgegeven')

	def validate_repeat_password(form, field):
		"""Only validate the repeat password if a password is set."""
		if len(form.password.data) > 0 and field.data != form.password.data:
			raise ValidationError('Wachtwoorden komen niet overeen')

class EditUserInfoForm(Form):
	""" Edit your own user information """
	id = IntegerField('ID')
	email = TextField('E-mail adres', validators=[Required(message='Geen emailadres opgegeven'), Email(message='Ongeldig emailadres opgegeven')])
	password = PasswordField('Wachtwoord')
	repeat_password = PasswordField('Herhaal wachtwoord')
	first_name = TextField('Voornaam', validators=[Required(message='Geen voornaam opgegeven')])
	last_name = TextField('Achternaam', validators=[Required(message='Geen achternaam opgegeven')])
	student_id = TextField('Studentnummer', validators=[Required(message='Geen studentnummer opgegeven')])
	education_id = SelectField('Opleiding', coerce=int)

	def validate_password(form, field):
		"""Providing a password is only required when creating a new user."""
		if form.id.data == 0 and len(field.data) == 0:
			raise ValidationError('Geen wachtwoord opgegeven')

	def validate_repeat_password(form, field):
		"""Only validate the repeat password if a password is set."""
		if len(form.password.data) > 0 and field.data != form.password.data:
			raise ValidationError('Wachtwoorden komen niet overeen')


class SignInForm(Form):
	email = TextField('E-mail adres', validators=[Required(), Email()])
	password = PasswordField('Wachtwoord', validators=[Required()])
	remember_me = BooleanField('Onthouden', default = False)

class ResetPassword(Form):
	email = TextField('E-mail adres', validators=[Required(message='Geen emailadres opgegeven'), Email(message='Ongeldig emailadres opgegeven')])
	student_id = TextField('Studentnummer', validators=[Required(message='Geen studentnummer opgegeven')])


#class EditUserPermissionEntry(Form):
#	select = SelectField(None, coerce=int, choices=[(1, 'Allow'), (-1, 'Deny'), (0, 'Inherit')])
#
#class EditUserPermissionForm(Form):
#	permissions = FieldList(FormField(EditUserPermissionEntry))
#	save_changes = SubmitField('Save changes')
