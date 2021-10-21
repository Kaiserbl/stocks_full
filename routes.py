from flask import render_template, request, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

from auth.forms import LoginForm
from auth.models import get_user

def setRoutes(app):
    @app.route("/")
    @app.route("/index")
    @login_required
    def index():
        return render_template('index.html')

    @app.route("/products")
    @login_required
    def editProduct():
        return render_template('product_edit.html', name='Muscle car model 7')

    @app.route("/users")
    @login_required
    def editUser():
        return render_template('user_edit.html', name='Sharon Hernandez')

    @app.route("/providers")
    @login_required
    def editProvider():
        return render_template('provider_edit.html', name='Santorini')

    @app.errorhandler(404)
    def error_404_handler(e):
        return render_template('404.html'), 404

    @app.route("/products/search")
    @login_required
    def searchProduct():
        return render_template('search_products.html', namePage="Products")

    @app.route("/users/search")
    @login_required
    def searchUsers():
        return render_template('search_users.html')
    
    @app.route("/providers/search")
    @login_required
    def searchProviders():
        return render_template('search_providers.html')
    
    @app.route('/product/detail')
    @login_required
    def home():
        return render_template('product_detail.html')
    
    @app.route('/provider/detail')
    @login_required
    def productos():
        return render_template('provider_detail.html')

    @app.route('/user/detail')
    @login_required
    def servicios():
        return render_template('user_detail.html')
    
    @app.route('/provider/new')
    @login_required
    def createprovider():
        return render_template('provider.html')
    
    @app.route('/product/new')
    @login_required
    def createproduct():
        return render_template('product.html')
    
    @app.route('/user/new')
    @login_required
    def createuser():
        return render_template('user.html')
    
    @app.route('/login', methods=["GET", "POST"])
    def login():
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        form = LoginForm()
        if form.validate_on_submit():
            user = get_user(form.email.data)
            if user is not None and user.check_password(form.password.data):
                login_user(user, remember=form.remember_me.data)
                next_page = request.args.get('next')
                if not next_page or url_parse(next_page).netloc != '':
                    next_page = url_for('index')
                return redirect(next_page)
        return render_template('login.html', form=form)
    
    @app.route('/dashboard')
    @login_required
    def dashboard():
        return render_template('dashboard.html')

    @app.route('/logout')
    def logout():
        logout_user()
        return redirect(url_for('index'))
    
    
