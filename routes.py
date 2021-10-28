from flask import render_template, request, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

from auth.forms import LoginForm
from auth.models import get_user

import sqlite3

def setRoutes(app):
    @app.route("/")
    @app.route("/index")
    @login_required
    def index():
        return render_template('index.html')

    # Routes for products
    @app.route("/products")
    @login_required
    def editProduct():
        return render_template('product_edit.html', name='Muscle car model 7')
    
    @app.route('/product/new')
    @login_required
    def createproduct():
        return render_template('product.html')
    
    @app.route('/savedproduct', methods=["GET", "POST"])
    def savedProduct():
        message = ""  
        if request.method == "POST":  
            with sqlite3.connect("stocks.db") as con: 
                try:  
                    name = request.form["Name"]
                    description = request.form["Description"]
                    cminima = int(request.form["MininumStock"])
                    current = int(request.form["CurrentStock"])
                    cur = con.cursor()  
                    cur.execute("INSERT INTO products (name, description, minimum_stock, current_stock) VALUES (?,?,?,?)",(name, description, cminima, current))  
                    con.commit()  
                except:  
                    con.rollback()   
                    message = "We can not add the product" 
                    flash(message) 
                finally:  
                    message = "Product successfully Added" 
                    flash(message)
                    return redirect("products/search", code = 302)  
                    con.close() 
    
    @app.route("/products/search")
    @login_required
    def searchProduct():
        con = sqlite3.connect("stocks.db")  
        con.row_factory = sqlite3.Row  
        cur = con.cursor()  
        cur.execute("select * from products")  
        products = cur.fetchall()
        return render_template('search_products.html', products=products, namePage="Products")

    @app.route('/product/<int:id>/detail')
    @login_required
    def productDetails(id):
        con = sqlite3.connect("stocks.db")  
        con.row_factory = sqlite3.Row  
        cur = con.cursor()  
        query = """SELECT * from products where id = ?"""
        cur.execute(query, (id,))  
        product = cur.fetchone()
        providersQuery = """SELECT * from providers"""
        cur.execute(providersQuery) 
        providers = cur.fetchall()
        return render_template('product_detail.html', product=product, providers=providers)

    @app.route('/product/<int:id>/delete')
    def deleteProduct(id):
        message = ""  
        with sqlite3.connect("stocks.db") as con: 
            try:
                cur = con.cursor()  
                deleteQuery = """DELETE FROM products WHERE id = ?"""
                cur.execute(deleteQuery, (id,))  
            except:  
                con.rollback()   
                message = "We can not delete the product" 
                flash(message) 
            finally:  
                message = "Product Deleted Successfully"
                flash(message)
                return render_template('search_products.html')
                con.close() 

    # Routes for providers
    @app.route("/providers")
    @login_required
    def editProvider():
        return render_template('provider_edit.html', name='Santorini')

    @app.route('/provider/new')
    @login_required
    def createprovider():
        return render_template('provider.html')

    @app.route('/savedprovider', methods=["GET", "POST"])
    def savedProvider():
        msg = ""  
        if request.method == "POST":  
            with sqlite3.connect("stocks.db") as con: 
                try:  
                    name = request.form["NameProvider"]
                    product = request.form["Product"]
                    email = request.form["EmailProvider"]
                    contactNumber = request.form["ContactNumber"]
                    cur = con.cursor()  
                    cur.execute("INSERT INTO providers (name, product, email, contact_number) VALUES (?,?,?,?)",(name, product, email, contactNumber))  
                    con.commit()  
                except:  
                    con.rollback()   
                    msg = "We can not add the provider"  
                    flash(msg)
                finally:  
                    msg = "Provider successfully Added"  
                    flash(msg)
                    return redirect("providers/search", code = 302)  
                    con.close()  
    
    @app.route("/providers/search")
    @login_required
    def searchProviders():
        con = sqlite3.connect("stocks.db")  
        con.row_factory = sqlite3.Row  
        cur = con.cursor()  
        cur.execute("select * from providers")  
        providers = cur.fetchall()
        return render_template('search_providers.html', providers=providers)

    @app.route('/provider/<int:id>/detail')
    @login_required
    def providerDetails(id):
        con = sqlite3.connect("stocks.db")  
        con.row_factory = sqlite3.Row  
        cur = con.cursor()  
        query = """SELECT * from providers where id = ?"""
        cur.execute(query, (id,))  
        provider = cur.fetchone()
        return render_template('provider_detail.html', provider=provider)

    @app.route('/provider/<int:id>/delete')
    def deleteProvider(id):
        message = ""  
        with sqlite3.connect("stocks.db") as con: 
            try:
                cur = con.cursor()  
                deleteQuery = """DELETE FROM providers WHERE id = ?"""
                cur.execute(deleteQuery, (id,))  
            except:  
                con.rollback()   
                message = "We can not delete the provider" 
                flash(message) 
            finally:  
                message = "Provider Deleted Successfully"
                flash(message)
                return render_template('search_providers.html')
                con.close()  

    # Routes for users
    @app.route("/users")
    @login_required
    def editUser():
        return render_template('user_edit.html', name='Sharon Hernandez')

    @app.route('/user/new')
    @login_required
    def createuser():
        return render_template('user.html')
    
    @app.route('/saveduser', methods=["GET", "POST"])
    def savedUser():
        msg = ""  
        if request.method == "POST":  
            with sqlite3.connect("stocks.db") as con: 
                try:  
                    firstName = request.form["FirstName"]
                    lastName = request.form["LastName"]
                    email = request.form["UserEmail"]
                    password = request.form["Password"]
                    role = request.form["Role"]
                    cur = con.cursor()  
                    cur.execute("INSERT INTO users (first_name, last_name, email, password, role) VALUES (?,?,?,?, ?)",(firstName, lastName, email, password, role))  
                    con.commit()    
                except:  
                    con.rollback()   
                    msg = "We can not add the user"
                    flash(msg)  
                finally:  
                    msg = "User successfully Added"
                    flash(msg)
                    return redirect("users/search", code = 302)
                    con.close()

    @app.route("/users/search")
    @login_required
    def searchUsers():
        con = sqlite3.connect("stocks.db")  
        con.row_factory = sqlite3.Row  
        cur = con.cursor()  
        cur.execute("select * from users")  
        users = cur.fetchall()
        return render_template('search_users.html', users=users)

    @app.route('/user/<int:id>/detail')
    @login_required
    def userDetails(id):
        con = sqlite3.connect("stocks.db")  
        con.row_factory = sqlite3.Row  
        cur = con.cursor()  
        query = """SELECT * from users where id = ?"""
        cur.execute(query, (id,))  
        user = cur.fetchone()
        return render_template('user_detail.html', user=user)

    @app.route('/user/<int:id>/delete')
    def deleteUser(id):
        message = ""  
        with sqlite3.connect("stocks.db") as con: 
            try:
                cur = con.cursor()  
                deleteQuery = """DELETE FROM users WHERE id = ?"""
                cur.execute(deleteQuery, (id,))  
            except:  
                con.rollback()   
                message = "We can not delete the user" 
                flash(message) 
            finally:  
                message = "User Deleted Successfully"
                flash(message)
                return render_template('search_users.html')
                con.close() 

    # Routes for other app sections
    @app.errorhandler(404)
    def error_404_handler(e):
        return render_template('404.html'), 404         
    
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