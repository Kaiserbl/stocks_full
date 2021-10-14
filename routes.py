from flask import render_template

def setRoutes(app):
    @app.route("/")
    def index():
        return render_template('index.html')

    @app.errorhandler(404)
    def error_404_handler(e):
        return render_template('404.html'), 404