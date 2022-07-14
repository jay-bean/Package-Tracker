from flask import Blueprint, render_template, redirect, url_for
from ..shipping_form import ShippingForm
bp = Blueprint('Main', __name__, url_prefix='')
from ..models import db, Package

@bp.route('/', methods=(['GET']))
def home():
  packages = Package.query.all()
  return render_template('package_status.html', packages=packages)

@bp.route('/new_package', methods=(['GET', 'POST']))
def new_package():
  form = ShippingForm()
  if form.validate_on_submit():
    data = form.data
    new_package = Package (
      name=data['sender'],
      recipient=data['recipient'],
      origin=data['origin'],
      destination=data['destination'],
      location=data['origin']
    )
    Package.advance_all_locations()
    db.session.add(new_package)
    db.session.commit()
    return redirect('/')
  return render_template('shipping_request.html', form=form)
