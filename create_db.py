

#####   Run this code before running the app
#####
#####   Default ADMIN credentials  =>  Employee ID : 1  ||  Password : ADMIN  (see last query)
#####


queries = (
    """
    CREATE TABLE IF NOT EXISTS employees (
        emp_id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL,
        email VARCHAR(255) UNIQUE,
        gender VARCHAR(40),
        birthday DATE,
        contact VARCHAR(255),
        salary INT,
        workshift VARCHAR(60),
        address VARCHAR(255),
        usertype VARCHAR(60) NOT NULL
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS sales (
        sale_id SERIAL,
        date TIMESTAMP,
        emp_id INT,
        product_name VARCHAR(255) NOT NULL,
        customer_name VARCHAR(255) NOT NULL,
        country VARCHAR(80) NOT NULL,
        address VARCHAR(255) NOT NULL,
        contact VARCHAR(255) NOT NULL,
        zip VARCHAR(40) NOT NULL,
        qty INT NOT NULL,
        total INT NOT NULL,
        PRIMARY KEY(sale_id),
        CONSTRAINT fk_employee
          FOREIGN KEY(emp_id)
            REFERENCES employees(emp_id)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS categories (
        cat_id SERIAL PRIMARY KEY,
        category VARCHAR(255) NOT NULL
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS suppliers (
        supp_id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        contact VARCHAR(255) NOT NULL,
        description VARCHAR(255) NOT NULL
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS products (
        product_id SERIAL PRIMARY KEY,
        product_name VARCHAR(255) NOT NULL,
        category VARCHAR(255) NOT NULL,
        supplier VARCHAR(255) NOT NULL,
        stock INT NOT NULL,
        price INT NOT NULL,
        unit VARCHAR(40) NOT NULL
    )
    """,
    """
    INSERT INTO employees(name, password, usertype) VALUES('ADMIN', 'ADMIN', 'admin')  
    """)


import credentials
import psycopg2

def db_init():
    try:
        with psycopg2.connect(**credentials.connection_params) as conn:
            with conn.cursor() as cursor:
                for query in queries:
                    cursor.execute(query)
                    conn.commit()
                print("DB: Tables succesfully initialised")
    except Exception as e:
        print(f"DB: Initialization failed ({e})")

db_init()