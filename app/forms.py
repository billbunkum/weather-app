from wtforms import (
    Form, 
    StringField,
    RadioField,
    validators,
)

class WeatherForm(Form):
    city = StringField("City", validators=[validators.DataRequired()])
    country_code = StringField("Country Code", 
        validators=[],
        render_kw={"maxlength": 2})
    units = RadioField("Units", 
        default='imperial',
        choices=[
            ('imperial', 'imperial', ),
            ('metric', 'metric',),
        ],
        validators=[validators.DataRequired()])