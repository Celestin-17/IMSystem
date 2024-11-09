# Inventory Management System

The Inventory Management System is a Python based GUI application using Tkinter and PostgresDB to streamline the tracking, organization, and control of inventory.
The system offers real-time insights into product and stock levels, sales records with automatically generated invoices and the ability to track and manage supplier and employee information.


The program operates on 2 User Access Levels: Admin and Employee. 


Employees have a separate dashboard with limited access, allowing them only to record sales and update their personal account settings such as email, phone number, and password.
Their dashboard provides real-time data on their total number of sales, generated revenue as well as current stock levels and product count. They can also utilize the search feature to find products and sales records.


The Admin Dashboard provides live data on total products, stock availability, total generated income and the overall number of sales. From there you can manage products, sales, employees, suppliers, and product categories.


# Program features:


• Optimized User Interface (since Tkinter graphics are slightly old aged, I edited and incorporated 70+ images for the UI Widgets)

• Login System  (based on EmployeeID that is given upon employee creation)

• Secured backend  (only parameterized queries executed from a separate DBHandler Class)

• Secured credentials  (environmental variables loaded from a separate .env file)

• Password Recovery  (email and date of birth are requested, after confirmation a new password is generated and sent to the account's email address)

• Dedicated pages for creating, managing, and updating products, sales, employees, suppliers, and product categories

• Separated Dashboards  (employees have limited access, they can only record sales, use the search feature and manage their account's settings)

• Create/Update Switch  (each time you select an item, update operations will be performed on it, to switch, you must click the 'reset' button)

• Automated Invoice Generator  (invoices will be generated into 'Invoices' folder and named by the customer's name upon recording the sale)

• Refresh Button  (reloads data on the table, it's automatically updated after performing any db operation but it's there just in case)

• Real-time data on the dashboard displaying total products, available stock, total sales, and total income generated

• Auto-Fill Entries  (selecting an item will automatically fill the entries with item's details)

• Search feature  (available on products and sales records, searching sales by employee id is also available)

• Account Settings Management  (you can change your email, password or phone number, for email changing a confirmation key will be sent to the new email address)

• Real-time updated timestamp at the bottom of every page


# Installation

- To set up your environment for launching the app, you need to create a .env file in the root directory of your project. There you need to fill in the credentials for your PostgreSQL database and the SMTP credentials.

- Once the .env file is created, you need to run create_db.py to initialize the db tables

- Therefore you can launch your application, the default admin login credentials:  EmployeeID: '1'  ||  Password: 'ADMIN'
- Creating an employee grants access permissions, to assign admin privileges, you must set their 'usertype' to 'admin'

- Before adding any products, you must create a category and have a supplier.

- Enjoy

# Screenshots


![Screenshot 2024-11-06 at 22 43 10](https://github.com/user-attachments/assets/ce2bf7a1-7cbd-4cb3-bac7-01b52e5d972c) 
![Screenshot 2024-11-07 at 13 12 40](https://github.com/user-attachments/assets/df5ce535-627e-4a06-85d3-faefead835da)
![Screenshot 2024-11-06 at 22 30 01](https://github.com/user-attachments/assets/891b82bc-266a-4f4a-b2eb-1d1a829bdcfd)
![Screenshot 2024-11-06 at 22 49 04](https://github.com/user-attachments/assets/b6226ae5-8c6b-479e-9fa3-a3429cfff47b)
![Screenshot 2024-11-06 at 22 48 37 (1)](https://github.com/user-attachments/assets/bd601076-dd5e-4110-b585-e0422faf335f)
![Screenshot 2024-11-06 at 22 43 21](https://github.com/user-attachments/assets/8193327e-93d7-4a21-b897-d256a6608e17)
![Screenshot 2024-11-06 at 23 14 49](https://github.com/user-attachments/assets/5d7dc0c5-dd81-4ead-a198-61d477509074)   
![Screenshot 2024-11-06 at 22 50 58](https://github.com/user-attachments/assets/0a609687-e345-424f-b7bf-758b6153f8ac)
![EmmaTaylor](https://github.com/user-attachments/assets/37222b9e-9703-4ca7-9dcc-7f34c2d1d646)

