from flask import Blueprint, render_template, redirect, url_for
from ..shipping_form import ShippingForm
bp = Blueprint('Main', __name__, url_prefix='')

@bp.route('/', methods=(['GET']))
def home():
  return render_template('base.html')

@bp.route('/new_package', methods=(['GET', 'POST']))
def new_package():
  form = ShippingForm()
  if form.validate_on_submit():
    return redirect('/')
  return render_template('shipping_request.html', form=form)
