from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class InputForm(FlaskForm):
    userInput = StringField('Amount: ', validators=[DataRequired(), Length(min=1, max =10000000)])
