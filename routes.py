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
    
    @app.route('/product/detail')
    def home():
        return render_template('product_detail.html')
    
    @app.route('/provider/detail')
    def productos():
        return render_template('provider_detail.html')

    @app.route('/user/detail')
    def servicios():
        return render_template('user_detail.html')