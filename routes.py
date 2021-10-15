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

    @app.route("/products/search")
    def searchProduct():
        return render_template('search_products.html')

    @app.route("/users/search")
    def searchUsers():
        return render_template('search_users.html')
    
    @app.route("/providers/search")
    def searchProviders():
        return render_template('search_providers.html')
    
    @app.route('/product/detail')
    def home():
        return render_template('product_detail.html')
    
    @app.route('/provider/detail')
    def productos():
        return render_template('provider_detail.html')

    @app.route('/user/detail')
    def servicios():
        return render_template('user_detail.html')
    
    @app.route('/provider/new')
    def createprovider():
        return render_template('provider.html')
    
    @app.route('/product/new')
    def createproduct():
        return render_template('product.html')
    
    @app.route('/user/new')
    def createuser():
        return render_template('user.html')
    
    @app.route('/login')
    def login():
        return render_template('login.html')
    
    @app.route('/dashboard')
    def dashboard():
        return render_template('dashboard.html')
    
    
