from flask.ext.wtf import Form, BooleanField, FormField, FieldList, SubmitField, \
		SelectField


class ModuleEditGroupPermissionEntry(Form):
	select = SelectField(None, coerce=int, choices=[(0, "Geen"), (1, "Lees"), (2, "Lees/Schrijf")])

class ModuleEditGroupPermissionForm(Form):
	permissions = FieldList(FormField(ModuleEditGroupPermissionEntry))
	save_changes = SubmitField('Sla veranderingen op')