from flask import render_template

def setRoutes(app):
    @app.route("/")
    def index():
        return render_template('index.html')

    @app.route("/products")
    def editProduct():
        return render_template('product_edit.html')

    @app.errorhandler(404)
    def error_404_handler(e):
        return render_template('404.html'), 404

    @app.route("/products/search")
    def searchProduct():
        return render_template('search_products.html')

    @app.route("/users/search")
    def searchUsers():
        return render_template('search_users.html')
    
    @app.route("/providers/search")
    def searchProviders():
        return render_template('search_providers.html')