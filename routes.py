from flask import render_template

def setRoutes(app):
    @app.route("/")
    def index():
        return render_template('index.html')

    @app.route("/products")
    def editProduct():
        return render_template('product_edit.html', name='Muscle car model 7')

    @app.route("/users")
    def editUser():
        return render_template('user_edit.html', name='Sharon Hernandez')

    @app.route("/providers")
    def editProvider():
        return render_template('provider_edit.html', name='Santorini')

    @app.errorhandler(404)
    def error_404_handler(e):
        return render_template('404.html'), 404