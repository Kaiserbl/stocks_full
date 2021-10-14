import routes
from flask import Flask

app = Flask(__name__, template_folder="templates")
routes.setRoutes(app)

if __name__ == "__main__":
    app.run()
