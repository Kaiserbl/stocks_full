import routes
from flask import Flask
from flask_login import LoginManager
from auth.models import users

app = Flask(__name__, template_folder="templates")
# TODO locate this properly
app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
login_manager = LoginManager(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    for user in users:
        if user.id == user_id:
            return user
    return None

routes.setRoutes(app)

if __name__ == "__main__":
    app.run()
