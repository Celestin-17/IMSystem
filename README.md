# Inventory Management System

The Inventory Management System is a Python based GUI application using Tkinter and PostgresDB to streamline the tracking, organization, and control of inventory.
The system provides real-time visibility into products and stock levels, sales records with automated invoice generation, along with the ability to track supplier and employee data.

The app operates with two distinct User Access Levels: ADMIN and Employee. 

Employees have a separate dashboard with limited access, allowing them only to record sales and update their personal settings such as email, address, and password.
Their dashboard provides real-time data on their number of sales, generated revenue, as well as current stock levels and product count. They can also utilize the search feature to find products and sales records.

The Admin Dashboard provides live data on total products, stock availability, total generated income and the overall number of sales. From there you can manage products, sales, employees, suppliers, and product categories. 

# Program features:

• Optimized User Interface : Since Tkinter graphics are very old aged I incorporated 70+ images for the UI Widgets and every button it's a label at base with 3 functions bound to act as one.
• Login System (based on EmployeeID that is given upon employees creation)
• Secured queries (only parameterized queries executed from a separate DBHandler Class)
• Password Recovery (new password is generated and sent to the accoount's email address)
