# Inventory Management System

The Inventory Management System is a Python based GUI application using Tkinter and PostgresDB to streamline the tracking, organization, and control of inventory.
The system offers real-time insights into product and stock levels, sales records with automatic invoice generation, and the ability to track supplier and employee information.


The program operates on 2 User Access Levels: ADMIN and Employee. 


Employees have a separate dashboard with limited access, allowing them only to record sales and update their personal settings such as email, address, and password.
Their dashboard provides real-time data on their number of sales, generated revenue, as well as current stock levels and product count. They can also utilize the search feature to find products and sales records.


The Admin Dashboard provides live data on total products, stock availability, total generated income and the overall number of sales. From there you can manage products, sales, employees, suppliers, and product categories.


# Program features:


• Optimized User Interface (since Tkinter graphics are very old aged I incorporated 70+ images for the UI Widgets)

• Login System  (based on EmployeeID that is given upon employee creation)

• Secured backend  (only parameterized queries executed from a separate DBHandler Class)

• Secured credentials  (environmental variables loaded from a separate .env file)

• Password Recovery  (email address and date of birth are being requested, afterwards a new password is generated and sent to the accoount's email address)

• Dedicated pages for creating, managing, and updating products, sales, employees, suppliers, and product categories

• Separated Dashboards  (employees have limited access, they can only record sales, use the search feature and manage their account's settings)

• Create/Update Switch  (each time you select an item, update operations will be performed on it, to switch, you must click the 'reset' button)

• Automated Invoice Generator  (will be created in 'Invoices' folder with the customer's name upon recording a sale)

• Refresh Button  (reloads data on the table, normally they are automatically updated but it's there just in case)

• Real-time data on the dashboard displaying total products, available stock, total sales, and total income generated

• Auto-Fill Entries  (selecting an item will automatically fill the entries with the item's details)

• Search feature  (available on products and sales records)

• Account Settings Page  (you can change your email, password or phone number, for email changing a confirmation key will be sent to the new email address)

• Real-time updated timestamp at bottom of every page


# Installation
 
