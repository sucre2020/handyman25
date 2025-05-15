from flask import Blueprint, render_template

handymen_bp = Blueprint('handymen', __name__)

@handymen_bp.route('/handymen')
def handymen():
    return render_template("handymen.html")