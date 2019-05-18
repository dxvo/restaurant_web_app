from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SelectField,PasswordField,SubmitField,BooleanField,DateField,widgets, SelectMultipleField, RadioField, FloatField
from wtforms.validators import DataRequired,Length,Email,EqualTo,NumberRange,Optional, InputRequired
from wtforms.widgets import PasswordInput, CheckboxInput, ListWidget, html_params, HTMLString
from wtforms.fields.html5 import DateField
from QueryEngine import QueryEngine
from datetime import date
import string
qe = QueryEngine()
qe.setup_default()



class ButtonWidget(object):
    input_type = 'submit'

    html_params = staticmethod(html_params)

    def __call__(self, field, **kwargs):
        kwargs.setdefault('id', field.id)
        kwargs.setdefault('type', self.input_type)
        if 'value' not in kwargs:
            kwargs['value'] = field._value()

        return HTMLString('<button {params}>{label}</button>'.format(
            params=self.html_params(name=field.name, **kwargs),
            label=field.label.text)
        )

class ButtonField(StringField):
    widget = ButtonWidget()


class LoginForm(FlaskForm):
    user = StringField('Username',
                        validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')



class SurveyForm(FlaskForm):
    first_name = StringField('FirstName',validators=[DataRequired()])
    sex = SelectField('Gender',choices=[('',''),('male','Male'),('female','Female')],validators=[DataRequired(),Length(min = 1)])
    ethnicity =  SelectField('Ethnicity',choices=[('',''),('WH','White'),
        ('AA','African American'),('AS','Asian'),('HI','Hispanic'),('OT','Others')],
        validators=[DataRequired(),Length(min = 1)])

    age = IntegerField('Age',validators=[DataRequired()])
    zipcode = IntegerField('Zip code',validators=[DataRequired()])
    
    submit = SubmitField('Submit')