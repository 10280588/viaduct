from flask.ext.wtf import Form
from wtforms import StringField, SelectField, SubmitField, DecimalField
from wtforms.validators import InputRequired, Email


class CreateForm(Form):
    name = StringField(u'Formulier naam')
    max_attendants = StringField(u'Maximale aantal deelnemers')
    msg_success = StringField(u'Succes bericht : Wordt getoond wanneer' +
                              'gebruiker zich inschrijft')
    origin = StringField(u'Who')
    html = StringField(u'Let the dogs out')
    email = StringField('E-mail', validators=[InputRequired(), Email()])
    first_name = StringField('First name', validators=[InputRequired()])
    last_name = StringField('Last name', validators=[InputRequired()])
    student_id = StringField('Student ID', validators=[InputRequired()])
    price = DecimalField('Price', places=2, validators=[InputRequired()])
    education_id = SelectField('Education', coerce=int)
    submit = SubmitField('Opslaan')
    transaction_description = StringField('Beschrijving van de transactie')
