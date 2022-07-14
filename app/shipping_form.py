from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from map.map import map

class ShippingForm(FlaskForm):
  sender = StringField('Sender', validators=[DataRequired()])
  recipient = StringField('Recipient', validators=[DataRequired()])
  origin = SelectField('Origin', choices=[k for k in map], validators=[DataRequired()])
  destination = SelectField('Destination', choices=[k for k in map], validators=[DataRequired()])
  express_shipping = BooleanField('Express Shipping')
  send = SubmitField('Send')
