from flask import Blueprint, render_template

handyman_sign_up_bp = Blueprint("handyman_sign_up", __name__)

@handyman_sign_up_bp.route("/handyman_sign_up")
def handyman_sign_up():
    return render_template("handyman-signup.html")