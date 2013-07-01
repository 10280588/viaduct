from viaduct import db

class Company(db.Model):
	__tablename__ = 'company'

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(256), unique=True)
	description = db.Column(db.String(1024))
	contract_start_date = db.Column(db.Date)
	contract_end_date = db.Column(db.Date)
	location_id = db.Column(db.Integer, db.ForeignKey('location.id'))
	contact_id = db.Column(db.Integer, db.ForeignKey('contact.id'))

	location = db.relationship('Location', backref=db.backref('companies',
			lazy='dynamic'))
	contact = db.relationship('Contact', backref=db.backref('companies',
			lazy='dynamic'))

	def __init__(self, title, description, contract_start_date,
			contract_end_date, location, contact):
		self.title = title
		self.description = description
		self.contract_start_date = contract_start_date
		self.contract_end_date = contract_end_date
		self.location = location
		self.contact = contact