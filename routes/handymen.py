from flask import Blueprint, render_template
from db.connection import handymen_collection

handymen_bp = Blueprint('handymen', __name__)

@handymen_bp.route('/handymen')
def handymen():
    handymen = handymen_collection.find()
    return render_template("handymen.html", handymen=handymen)