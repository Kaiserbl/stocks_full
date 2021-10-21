import sqlite3  
  
con = sqlite3.connect("stocks.db")  
print("Database Created Successfully")  
  
con.execute("create table products (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, description TEXT NOT NULL, minimum_stock INT NOT NULL, current_stock INT NOT NULL)")  
  
print("Products Table Created Successfully")  

con.execute("create table providers (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, product TEXT NOT NULL, email TEXT UNIQUE NOT NULL, contact_number TEXT NOT NULL)")
  
print("Providers Table Created Successfully")  

con.execute("create table users (id INTEGER PRIMARY KEY AUTOINCREMENT, first_name TEXT NOT NULL, last_name TEXT NOT NULL, email TEXT UNIQUE NOT NULL, role TEXT NOT NULL, password CHAR NOT NULL)")
  
print("Users Table Created Successfully")  
  
con.close()  
