from flask import Flask, render_template
from routes.index import index_bp
from routes.handymen import handymen_bp
from routes.profile import profile_bp
from routes.handyman_sign_up import handyman_sign_up_bp
from routes.about import about_bp

app = Flask(__name__)

app.register_blueprint(index_bp)
app.register_blueprint(handymen_bp)
app.register_blueprint(profile_bp)
app.register_blueprint(handyman_sign_up_bp)
app.register_blueprint(about_bp)

if __name__ == '__main__':
    app.run(debug=True)