import tkinter as tk
from psycopg2.sql import Identifier
import psycopg2
from psycopg2 import sql
import credentials


class DBHandler():
    """ Intermediates db operations between the app and postgres db """
    def __init__(self, parent):
        self.parent = parent
        self.db_params = credentials.connection_params


    def login(self, credentials):
        self.credentials = credentials
        self.emp_id = self.credentials[0]
        self.user_pass = self.credentials[1]
        try:
            with psycopg2.connect(**self.db_params) as conn:
                with conn.cursor() as cursor:
                    self.sql = """SELECT name, usertype FROM employees WHERE emp_id = %s AND password = %s"""
                    self.params = (self.emp_id, self.user_pass)
                    cursor.execute(self.sql, self.params)
                    self.data = cursor.fetchall()
                    if len(self.data) == 0: return False
                    else: return self.data
        except Exception as e:
            print(f"DB: Error encountered ({e})")

    def search_sale(self, method, target):
        self.method = method
        self.target = target
        try:
            with psycopg2.connect(**self.db_params) as conn:
                with conn.cursor() as cursor:
                    if self.method == "product_name" or self.method == "customer_name":
                        self.sql = sql.SQL("""SELECT * FROM sales WHERE {} LIKE %s""")
                        cursor.execute(self.sql.format(Identifier(self.method)), (f"%{self.target}%",))
                        self.response = cursor.fetchall()
                        return self.response
                    elif self.method == "date":
                        self.sql = sql.SQL("""SELECT * FROM sales WHERE {} >= %s""")
                        cursor.execute(self.sql.format(Identifier(self.method)), (self.target,))
                        self.response = cursor.fetchall()
                        return self.response
                    else:
                        self.sql = sql.SQL("""SELECT * FROM sales WHERE {} = %s""")
                        cursor.execute(self.sql.format(Identifier(self.method)), (self.target,))
                        self.response = cursor.fetchall()
                        return self.response
        except Exception as e:
            print(f"DB: Error encountered ({e})")

    def search_product(self, method, target):
        self.method = method
        self.target = target
        try:
            with psycopg2.connect(**self.db_params) as conn:
                with conn.cursor() as cursor:
                    if self.method == "product_id":
                        self.sql = sql.SQL("""SELECT * FROM products WHERE {} = %s""")
                        cursor.execute(self.sql.format(Identifier(self.method)), (self.target,))
                        self.response = cursor.fetchall()
                        return self.response
                    else:
                        self.sql = sql.SQL("""SELECT * FROM products WHERE {} LIKE %s""")
                        cursor.execute(self.sql.format(Identifier(self.method)), (f"%{self.target}%",))
                        self.response = cursor.fetchall()
                        return self.response
        except Exception as e:
            print(f"DB: Error encountered ({e})")

    def remove_product(self, item):
        self.item = item
        try:
            with psycopg2.connect(**self.db_params) as conn:
                with conn.cursor() as cursor:
                    self.sql = """DELETE FROM products WHERE product_id = %s"""
                    cursor.execute(self.sql, (self.item,))
                    if cursor.rowcount > 0: return True
                    else: return False
        except Exception as e:
            print(f"DB: Encountered error ({e})")

    def add_employee(self, container):
        self.i = container
        try:
            with psycopg2.connect(**self.db_params) as conn:
                with conn.cursor() as cursor:
                    self.sql = """INSERT INTO employees(name, password, email, gender, birthday, contact,
                    salary, workshift, address, usertype) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                    self.params = (self.i[0], self.i[1], self.i[2], self.i[3], self.i[4], self.i[5],
                                   self.i[6], self.i[7], self.i[8], self.i[9])
                    cursor.execute(self.sql, self.params)
                    self.response = cursor.rowcount
        except Exception as e:
            print(f"DB: Error encountered ({e})")
        try:
            with psycopg2.connect(**self.db_params) as conn:
                with conn.cursor() as cursor:
                    self.sql = """SELECT * FROM employees WHERE name = %s AND birthday = %s"""
                    cursor.execute(self.sql, (self.i[0], self.i[4]))
                    self.response = cursor.fetchall()
                    self.emp_id = self.response[0][0]
                    if cursor.rowcount != 0: return self.emp_id
                    else: return False
        except Exception as e:
            print(f"DB: Error encountered ({e})")

    def update_employee(self, container):
        self.i = container
        try:
            with psycopg2.connect(**self.db_params) as conn:
                with conn.cursor() as cursor:
                    self.sql = """UPDATE employees SET name = %s, password = %s, email = %s, gender = %s, birthday = %s,
                    contact = %s, salary = %s, workshift = %s, address = %s, usertype = %s WHERE emp_id = %s"""
                    self.params = (self.i[0], self.i[1], self.i[2], self.i[3], self.i[4], self.i[5],
                                   self.i[6], self.i[7], self.i[8], self.i[9], self.i[10])
                    cursor.execute(self.sql, self.params)
                    self.response = cursor.rowcount
                    if self.response > 0: return True
                    else: return False
        except Exception as e:
            print(f"DB: Error encountered ({e})")

    def get_empsales(self, emp_id):
        """ Returns the dashboard's total number of sales made by an employee """
        self.emp_id = emp_id
        try:
            with psycopg2.connect(**self.db_params) as conn:
                with conn.cursor() as cursor:
                    self.sql = """SELECT COUNT(*) FROM sales WHERE emp_id = %s;"""
                    cursor.execute(self.sql, (self.emp_id,))
                    self.response = cursor.fetchall()
                    return self.response
        except Exception as e:
            print(f"DB: Error encountered ({e})")

    def generated_revenue(self, emp_id):
        self.emp_id = emp_id
        try:
            with psycopg2.connect(**self.db_params) as conn:
                with conn.cursor() as cursor:
                    self.sql = """SELECT total FROM sales WHERE emp_id = %s"""
                    cursor.execute(self.sql, (self.emp_id,))
                    self.response = cursor.fetchall()
                    return self.response
        except Exception as e:
            print(f"DB: Error encountered ({e})")

    def add_supplier(self, container):
        self.i = container
        try:
            with psycopg2.connect(**self.db_params) as conn:
                with conn.cursor() as cursor:
                    self.sql = """INSERT INTO suppliers(name, contact, description) VALUES(%s, %s, %s)"""
                    self.params = (self.i[0], self.i[1], self.i[2])
                    cursor.execute(self.sql, self.params)
                    self.response = cursor.rowcount
                    if self.response > 0: return True
                    else: return False
        except Exception as e:
            print(f"DB: Error encountered ({e})")

    def update_supplier(self, container):
        self.i = container
        try:
            with psycopg2.connect(**self.db_params) as conn:
                with conn.cursor() as cursor:
                    self.sql = """UPDATE suppliers SET name = %s, contact = %s, description = %s
                    WHERE supp_id = %s"""
                    self.params = (self.i[0], self.i[1], self.i[2], self.i[3])
                    cursor.execute(self.sql, self.params)
                    self.response = cursor.rowcount
                    if self.response > 0: return True
                    else: return False
        except Exception as e:
            print(f"DB: Error encountered ({e})")

    def remove_supplier(self, id):
        self.id = id
        try:
            with psycopg2.connect(**self.db_params) as conn:
                with conn.cursor() as cursor:
                    self.sql = """DELETE FROM suppliers WHERE supp_id = %s"""
                    cursor.execute(self.sql, (self.id,))
                    self.response = cursor.rowcount
                    if self.response > 0: return True
                    else: return False
        except Exception as e:
            print(f"DB: Error encountered ({e})")

    def remove_employee(self, container):
        self.container = container
        try:
            with psycopg2.connect(**self.db_params) as conn:
                with conn.cursor() as cursor:
                    self.sql = """DELETE FROM employees WHERE emp_id = %s"""
                    cursor.execute(self.sql, (self.container,))
                    self.response = cursor.rowcount
                    if self.response > 0: return True
                    else: return False
        except Exception as e:
            print(f"DB: Error encountered ({e})")

    def stock_count(self):
        self.stock = 0
        try:
            with psycopg2.connect(**self.db_params) as conn:
                with conn.cursor() as cursor:
                    self.sql = """SELECT stock FROM products"""
                    cursor.execute(self.sql)
                    self.data = cursor.fetchall()
                    for tuple in self.data:
                        self.stock += tuple[0]
                    return self.stock
        except Exception as e:
            print(f"DB: Error encountered ({e})")

    def get_products(self):
        try:
            with psycopg2.connect(**self.db_params) as conn:
                with conn.cursor() as cursor:
                    query = """SELECT * FROM products ORDER BY product_id ASC"""
                    cursor.execute(query)
                    self.products = cursor.fetchall()
                    return self.products
        except Exception as e:
            print(f"DB : Error encountered ({e})")

    def sales_record(self):
        try:
            with psycopg2.connect(**self.db_params) as conn:
                with conn.cursor() as cursor:
                    cursor.execute("""SELECT * FROM sales""")
                    self.data = cursor.fetchall()
                    return self.data
        except Exception as e:
            print(f"DB : Error encountered ({e})")

    def add_product(self, container):
        self.i = container
        self.sql = f"""INSERT INTO products(product_name, category, supplier, stock, price, unit)
        VALUES(%s, %s, %s, %s, %s, %s)"""
        self.params = (self.i[0], self.i[1], self.i[2], self.i[3], self.i[4], self.i[5])
        try:
            with psycopg2.connect(**self.db_params) as conn:
                with conn.cursor() as cursor:
                    cursor.execute(self.sql, self.params)
                    if cursor.rowcount > 0: return True
                    else: return False
        except Exception as e:
            print(f"DB: Error encountered ({e})")

    def update_product(self, container):
        self.i = container
        try:
            with psycopg2.connect(**self.db_params) as conn:
                with conn.cursor() as cursor:
                    self.sql = sql.SQL("""UPDATE products SET product_name = %s, category = %s, supplier = %s,
                    price = %s, stock = %s, unit = %s WHERE product_id = %s""")
                    self.params = (self.i[0], self.i[1], self.i[2], self.i[3], self.i[4], self.i[5], self.i[6])
                    cursor.execute(self.sql, self.params)
                    self.response = cursor.rowcount
                    if self.response > 0: return True
                    else: return False
        except Exception as e:
            print(f"DB: Error encountered ({e})")

    def get_rowcount(self):
        try:
            with (psycopg2.connect(**self.db_params) as conn):
                with conn.cursor() as cursor:
                    query = "SELECT * FROM products"
                    cursor.execute(query)
                    self.row_count = len(cursor.fetchall())
                    return self.row_count
        except Exception as e:
            print(f"DB: Error encountered ({e})")

    def update_category(self, container):
        self.i = container
        try:
            with psycopg2.connect(**self.db_params) as conn:
                with conn.cursor() as cursor:
                    self.sql = """UPDATE categories SET category = %s WHERE cat_id = %s"""
                    cursor.execute(self.sql, (self.i[0], self.i[1]))
                    self.response = cursor.rowcount
                    if self.response > 0: return True
                    else: return False
        except Exception as e:
            print(f"DB: Error encountered ({e})")

    def add_category(self, category):
        self.category = category
        try:
            with psycopg2.connect(**self.db_params) as conn:
                with conn.cursor() as cursor:
                    cursor.execute("""INSERT INTO categories(category) VALUES(%s)""", (self.category,))
                    self.response = cursor.rowcount
                    if self.response > 0: return True
                    else: return False
        except Exception as e:
            print(f"DB: Error encountered ({e})")

    def remove_category(self, id):
        self.id = id
        try:
            with psycopg2.connect(**self.db_params) as conn:
                with conn.cursor() as cursor:
                    self.sql = """DELETE FROM categories WHERE cat_id = %s"""
                    cursor.execute(self.sql, (self.id,))
                    self.response = cursor.rowcount
                    if self.response > 0: return True
                    else: return False
        except Exception as e:
            print(f"DB: Error encountered ({e})")

    def get_userdata(self, emp_id):
        self.emp_id = emp_id
        try:
            with psycopg2.connect(**self.db_params) as conn:
                with conn.cursor() as cursor:
                    self.sql = """SELECT * FROM employees WHERE emp_id = %s"""
                    cursor.execute(self.sql, (self.emp_id,))
                    self.response = cursor.fetchall()
                    return self.response
        except Exception as e:
            print(f"DB: Error encountered ({e})")

    def get_catdata(self):
        """Fetching categories names for Category Combobox"""
        try:
            with psycopg2.connect(**self.db_params) as conn:
                with conn.cursor() as cursor:
                    self.sql = """SELECT category FROM categories"""
                    cursor.execute(self.sql)
                    self.response = cursor.fetchall()
                    return self.response
        except Exception as e:
            print(f"DB: Error encountered ({e})")

    def get_categories(self):
        try:
            with psycopg2.connect(**self.db_params) as conn:
                with conn.cursor() as cursor:
                    self.query = """SELECT * FROM categories ORDER BY cat_id ASC"""
                    cursor.execute(self.query)
                    self.data = cursor.fetchall()
                    return self.data
        except Exception as e:
            print(f"DB: Error encountered ({e})")

    def update_password(self, container):
        self.i = container
        try:
            with psycopg2.connect(**self.db_params) as conn:
                with conn.cursor() as cursor:
                    self.sql = """UPDATE employees SET password = %s WHERE emp_id = %s"""
                    cursor.execute(self.sql, (self.i[0], self.i[1]))
                    self.response = cursor.rowcount
                    if self.response > 0: return True
                    else: return False
        except Exception as e:
            print(f"DB: Error encountered ({e})")

    def update_email(self, email, emp_id):
        self.email = email
        self.emp_id = emp_id
        try:
            with psycopg2.connect(**self.db_params) as conn:
                with conn.cursor() as cursor:
                    self.sql = """UPDATE employees SET email = %s WHERE emp_id = %s"""
                    cursor.execute(self.sql, (self.email, self.emp_id))
                    self.response = cursor.rowcount
                    if self.response > 0: return True
                    else: return False
        except Exception as e:
            print(f"DB: Error encountered ({e})")

    def update_phone(self, phone, emp_id):
        self.phone = phone
        self.emp_id = emp_id
        try:
            with psycopg2.connect(**self.db_params) as conn:
                with conn.cursor() as cursor:
                    self.sql = """UPDATE employees SET contact = %s WHERE emp_id = %s"""
                    cursor.execute(self.sql, (self.phone, self.emp_id))
                    self.response = cursor.rowcount
                    if self.response > 0: return True
                    else: return False
        except Exception as e:
            print(f"DB: Error encountered ({e})")

    def get_userpass(self, emp_id):
        self.emp_id = emp_id
        try:
            with psycopg2.connect(**self.db_params) as conn:
                with conn.cursor() as cursor:
                    self.sql = """SELECT password FROM employees WHERE emp_id = %s"""
                    cursor.execute(self.sql, (self.emp_id,))
                    self.response = cursor.fetchall()
                    return self.response
        except Exception as e:
            print(f"DB: Error encountered ({e})")

    def check_email(self, email):
        self.email = email
        try:
            with psycopg2.connect(**self.db_params) as conn:
                with conn.cursor() as cursor:
                    self.sql = """SELECT birthday, emp_id FROM employees WHERE email = %s"""
                    cursor.execute(self.sql, (self.email,))
                    self.response = cursor.fetchall()
                    if len(self.response) == 0: return False
                    else: return self.response
        except Exception as e:
            print(f"DB: Error encountered ({e})")


    def get_suppliers(self):
        try:
            with psycopg2.connect(**self.db_params) as conn:
                with conn.cursor() as cursor:
                    self.query = """SELECT * FROM Suppliers ORDER BY supp_id ASC"""
                    cursor.execute(self.query)
                    self.data = cursor.fetchall()
                    return self.data
        except Exception as e:
            print(f"DB: Error encountered ({e})")

    def user_state(self, emp_id:int):  # Checks if user is admin or an employee
        self.emp_id = emp_id
        try:
            with psycopg2.connect(**self.db_params) as conn:
                with conn.cursor() as cursor:
                    self.sql = f"""SELECT usertype FROM employees WHERE emp_id = %s"""
                    cursor.execute(self.sql, (self.emp_id,))
                    self.data = cursor.fetchall()
                    if self.data[0][0].lower() == "admin": return True
                    else: return False
        except Exception as e:
            print(f"DB: Error encountered ({e})")

    def load_emptree(self):  # Loads employees table
        try:
            with psycopg2.connect(**self.db_params) as conn:
                with conn.cursor() as cursor:
                    self.query = """SELECT * FROM employees ORDER BY emp_id ASC"""
                    cursor.execute(self.query)
                    self.data = cursor.fetchall()
                    return self.data
        except Exception as e:
            print(f"DB: Error encountered ({e})")

    def sales_record(self):  # Loads Sales Records table
        try:
            with psycopg2.connect(**self.db_params) as conn:
                with conn.cursor() as cursor:
                    cursor.execute("""SELECT * FROM sales ORDER BY sale_id ASC""")
                    self.data = cursor.fetchall()
                    return self.data
        except Exception as e:
            print(f"DB: Error encountered ({e})")


    def get_empid(self, user):
        self.user = user
        try:
            with psycopg2.connect(**self.db_params) as conn:
                with conn.cursor() as cursor:
                    self.query = f"""SELECT * FROM employees WHERE name = %s"""
                    cursor.execute(self.query, (self.user,))
                    self.data = cursor.fetchall()
                    print(self.data)
                    self.empid = self.data[0][0]
                    return self.empid
        except Exception as e:
            print(f"DB: Error encountered ({e})")

    def get_price(self, product):
        self.product = product
        try:
            with psycopg2.connect(**self.db_params) as conn:
                with conn.cursor() as cursor:
                    self.sql = """SELECT price FROM products WHERE product_name = %s"""
                    cursor.execute(self.sql, (self.product,))
                    self.data = cursor.fetchall()
                    return self.data
        except Exception as e:
            print(f"DB: Error encountered ({e})")

    def add_entry(self, container):
        self.i = container
        self.timestamp = self.i[0]
        try:
            with psycopg2.connect(**self.db_params) as conn:
                with conn.cursor() as cursor:
                    print(f"date is: {self.i[0]}")
                    self.sql = """INSERT INTO sales(date, emp_id, product_name, customer_name, country, address, 
                                contact, zip, total, qty) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                    self.params = (self.i[0], self.i[1], self.i[2], self.i[3], self.i[4], self.i[5], self.i[6],
                                   self.i[7], self.i[8], self.i[9])
                    cursor.execute(self.sql, self.params)
                    self.response = cursor.rowcount
                    if self.response > 0: return True
                    else: return False
        except Exception as e:
            print(f"DB: Error encountered ({e})")
        try:
            with psycopg2.connect(**self.db_params) as conn:
                with conn.cursor() as cursor:
                    self.sql = """SELECT sale_id FROM sales WHERE date = %s"""
                    cursor.execute(self.sql, (self.values["timestamp"],))
                    self.response = cursor.fetchall()
                    tk.messagebox.showinfo("Stock Manager", f"You have succesfully recorded Sale ID:{self.response[0][0]}")
                    return self.response[0][0]
        except Exception as e:
            print(f"DB: Error encountered ({e})")


    def update_sales(self, update):
        self.update = update
        self.phone = f"+{self.update["prefix"][1:3]}{self.update["phone"]}"
        print(f"phone is: {self.phone}")
        try:
            with psycopg2.connect(**self.db_params) as conn:
                with conn.cursor() as cursor:
                    self.sql = """UPDATE sales SET product_name = %s, customer_name = %s, country = %s, address = %s,
                    contact = %s, zip = %s, total = %s, qty = %s WHERE sale_id = %s"""
                    self.params = (self.update["pname"], self.update["cname"], self.update["country"],
                                   self.update["address"], self.phone, self.update["zip"],
                                   self.update["total"], self.update["qty"], self.update["id"])
                    cursor.execute(self.sql, self.params)
                    self.response = cursor.rowcount
                    if self.response != 0: return True
                    else: return False
        except Exception as e:
            print(f"DB: Error encountered ({e})")

    def total_sales(self):
        try:
            with psycopg2.connect(**self.db_params) as conn:
                with conn.cursor() as cursor:
                    cursor.execute("""SELECT COUNT(*) FROM sales""")
                    self.response = cursor.fetchall()
                    return self.response
        except Exception as e:
            print(f"DB: Error encountered ({e})")

    def total_income(self):
        try:
            with psycopg2.connect(**self.db_params) as conn:
                with conn.cursor() as cursor:
                    self.sql = """SELECT total FROM sales"""
                    cursor.execute(self.sql)
                    self.response = cursor.fetchall()
                    return self.response
        except Exception as e:
            print(f"DB: Error encountered ({e})")

    def remove_sale(self, saleid):
        self.saleid = saleid
        try:
            with psycopg2.connect(**self.db_params) as conn:
                with conn.cursor() as cursor:
                    self.sql = """DELETE FROM sales WHERE sale_id = %s"""
                    cursor.execute(self.sql, (self.saleid,))
                    if cursor.rowcount > 0: return True
                    else: return False
        except Exception as e:
            print(f"DB: Error encountered ({e})")















