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
    
    @app.route('/provider/new')
    def createprovider():
        return render_template('provider.html')
    
    @app.route('/product/new')
    def createproduct():
        return render_template('product.html')
    
    @app.route('/user/new')
    def createuser():
        return render_template('user.html')