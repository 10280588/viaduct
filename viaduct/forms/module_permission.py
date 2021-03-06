from flask_wtf import Form
from wtforms import FormField, FieldList, SubmitField, SelectField

from wtforms import Form as UnsafeForm


class ModuleEditGroupPermissionEntry(UnsafeForm):
    select = SelectField(None, coerce=int, choices=[(0, "Geen"), (1, "Lees"),
                                                    (2, "Lees/Schrijf")])


class ModuleEditGroupPermissionForm(Form):
    permissions = FieldList(FormField(ModuleEditGroupPermissionEntry))
    save_changes = SubmitField('Sla veranderingen op')
