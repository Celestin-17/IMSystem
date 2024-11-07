import tkinter as tk
from tkinter import PhotoImage
from tkinter import ttk
import datetime as dt
import pytz
import credentials
import empFrame
import categoriesFrame
import mainFrame
import dbHandler
import registerFrame
import settingsFrame
import suppliersFrame


class AdminFrame():
    """ Initializes Admin Dashboard Frame (only for Admins) """
    def __init__(self, parent, user, isAdmin:bool, emp_id:int):
        self.parent = parent
        self.user = user
        self.isAdmin = isAdmin
        self.emp_id = emp_id
        self.db_params = credentials.connection_params
        self.income_intvar = tk.IntVar()
        self.sales_intvar = tk.IntVar()
        self.stock_intvar = tk.IntVar()
        self.products_intvar = tk.IntVar()
        self.updating = False
        self.timezone = pytz.timezone("Europe/Bucharest")
        self.title_img = PhotoImage(file="./images/admin_dboard.png")
        self.passlabel_img = PhotoImage(file="./images/passlabel_img.png")
        self.userlabel_img = PhotoImage(file="./images/userlabel_img.png")
        self.or_label_img = PhotoImage(file="./images/or_label_img.png")
        self.title2_img = PhotoImage(file="./images/user.png")
        self.regimg = PhotoImage(file="./images/regimg.png")
        self.login_button_img = PhotoImage(file="./images/arrow.png")
        self.signup_img = PhotoImage(file="./images/signup_img.png")
        self.cpass_img = PhotoImage(file="./images/confirm.png")
        self.mail_img = PhotoImage(file="./images/email.png")
        self.back_img = PhotoImage(file="./images/back.png")
        self.stock_heading = PhotoImage(file="./images/admin_dboard.png")
        self.refresh_img = PhotoImage(file="./images/refresh.png")
        self.logout_img = PhotoImage(file="./images/logout.png")
        self.logout_label_img = PhotoImage(file="./images/logout_label.png")
        self.add_img = PhotoImage(file="./images/add.png")
        self.remove_img = PhotoImage(file="./images/remove.png")
        self.reset_img = PhotoImage(file="./images/undo.png")
        self.pname_img = PhotoImage(file="./images/pname.png")
        self.findby_img = PhotoImage(file="./images/findby.png")
        self.search_img = PhotoImage(file="./images/search.png")
        self.category_img = PhotoImage(file="./images/category.png")
        self.supplier_img = PhotoImage(file="./images/supplier.png")
        self.price_img = PhotoImage(file="./images/price.png")
        self.stock_img = PhotoImage(file="./images/stock.png")
        self.unit_img = PhotoImage(file="./images/unit.png")
        self.db_params = {
            "database" : "postgres",
            "user" : "Celestin",
            "password" : "10august",
            "host" : "localhost",
            "port" : "5432"
        }
        self.GUI()

    def GUI(self):
        self.bgcolor = "#ecebeb"
        self.frame = tk.Frame(self.parent, height=900, width=900, bg=self.bgcolor)
        self.frame.pack()
        self.label = tk.Label(self.parent, image=self.stock_heading, bg=self.bgcolor)
        self.label.place(x=150, y=20)
        self.today = dt.datetime.today()
        self.style = ttk.Style(self.parent)
        self.style.theme_use("clam")
        self.style.configure("Treeview", background="white", foreground="black", fieldbackground="white")
        self.tree = ttk.Treeview(self.parent, height=15, columns=4)
        self.tree["columns"] = ("ProductID", "Product", "Category", "Supplier", "Selling price", "Stock", "Unit")
        self.tree.column("#0", width=0, minwidth=0)
        self.tree.column("ProductID", width=65, minwidth=65)
        self.tree.column("Product", width=170, minwidth=100)
        self.tree.column("Category", width=130, minwidth=90)
        self.tree.column("Supplier", width=130, minwidth=90)
        self.tree.column("Selling price", width=90, minwidth=50)
        self.tree.column("Stock", width=75, minwidth=75)
        self.tree.column("Unit", width=75, minwidth=75)

        self.tree.heading("#0", text="Label", anchor="w")
        self.tree.heading("ProductID", text="ProductID")
        self.tree.heading("Product", text="Product")
        self.tree.heading("Category", text="Category")
        self.tree.heading("Supplier", text="Supplier")
        self.tree.heading("Selling price", text="Selling price")
        self.tree.heading("Stock", text="Stock")
        self.tree.heading("Unit", text="Unit")
        self.refresh_img = self.refresh_img.subsample(2, 2)
        self.refresh_label = tk.Label(self.parent, image=self.refresh_img, background=self.bgcolor)
        self.refresh_label.place(x=835, y=350)
        self.pname_label = tk.Label(self.parent, image=self.pname_img, bg=self.bgcolor)
        self.pname_label.place(x=95, y=540)
        self.totalprods_label = tk.Label(self.parent, text="Total products: ", bg=self.bgcolor, fg="black",
                                         font=("Arial", 20, "bold"))
        self.totalprods_label.place(x=130, y=740)
        self.total_label = tk.Label(self.parent, font=("Arial", 20, "bold"), bg=self.bgcolor, fg="blue",
                                    textvariable=self.products_intvar)
        self.total_label.place(x=285, y=740)
        self.available_stock_label = tk.Label(self.parent, text="Available stock: ", bg=self.bgcolor, fg="black",
                                              font=("Arial", 20, "bold"))
        self.available_stock_label.place(x=130, y=775)
        self.stock_label2 = tk.Label(self.parent, font=("Arial", 20, "bold"), bg=self.bgcolor, fg="blue",
                                     textvariable=self.stock_intvar)
        self.stock_label2.place(x=295, y=775)
        self.total_income_label = tk.Label(self.parent, text=f"Total income:", font=("Arial", 20, "bold"),
                                            bg=self.bgcolor, fg="black")
        self.total_income_label.place(x=130, y=807)
        self.income_label = tk.Label(self.parent, textvariable=self.income_intvar, font=("Arial", 20, "bold"),
                                      bg=self.bgcolor, fg="blue")
        self.income_label.place(x=270, y=807)
        self.total_sales = tk.Label(self.parent, text=f"Total sales:", font=("Arial", 20, "bold"), bg=self.bgcolor,
                                    fg="black")
        self.total_sales.place(x=130, y=840)
        self.sales_label = tk.Label(self.parent, textvariable=self.sales_intvar, font=("Arial", 20, "bold"),
                                    bg=self.bgcolor, fg="blue")
        self.sales_label.place(x=250, y=840)
        self.welcome_label = tk.Label(self.parent, text=f"Welcome back, {self.user} !", font=("Arial", 25, "italic"),
                                       background=self.bgcolor, bg=self.bgcolor, fg="black")
        self.welcome_label.place(x=160, y=685)
        self.today_header = tk.Label(self.parent, text="", bg=self.bgcolor, foreground="black", font=("Arial", 14, "italic"))
        self.today_header.place(x=675, y=875)
        self.timenow_header = tk.Label(self.parent, text="", bg=self.bgcolor, foreground="black",
                                       font=("Arial", 14, "italic"))
        self.timenow_header.place(x=592, y=875)
        self.logout_img = self.logout_img.subsample(2, 2)
        self.logout = tk.Label(self.parent, image=self.logout_img, background=self.bgcolor)
        self.logout.place(x=810, y=55)
        self.logout_label_img = self.logout_label_img.subsample(2, 2)
        self.logout_label = ttk.Label(self.parent, image=self.logout_label_img, background=self.bgcolor)
        self.logout_label.place(x=783, y=10)
        self.findby_label = tk.Label(self.parent, image=self.findby_img, bg=self.bgcolor)
        self.findby_label.place(x=540, y=625)
        self.supplier_label = tk.Label(self.parent, image=self.supplier_img, bg=self.bgcolor)
        self.supplier_label.place(x=465, y=543)
        self.price_label = tk.Label(self.parent, image=self.price_img, bg=self.bgcolor)
        self.price_label.place(x=611, y=547)
        self.unit_label = tk.Label(self.parent, image=self.unit_img, bg=self.bgcolor)
        self.unit_label.place(x=763, y=545)
        self.back_img = self.back_img.subsample(2, 2)
        self.add_img = self.add_img.subsample(2, 2)
        self.add_label = tk.Label(self.parent, image=self.add_img, bg=self.bgcolor)
        self.add_label.place(x=130, y=625)
        self.remove_img = self.remove_img.subsample(2, 2)
        self.remove_label = tk.Label(self.parent, image=self.remove_img, bg=self.bgcolor)
        self.remove_label.place(x=290, y=625) ## +70
        self.reset_label = tk.Label(self.parent, image=self.reset_img, bg=self.bgcolor)
        self.reset_label.place(x=440, y=625)
        self.search_img = self.search_img.subsample(2, 2)
        self.search_label = tk.Label(self.parent, image=self.search_img, bg=self.bgcolor)
        self.search_label.place(x=650, y=790)
        self.category_label = tk.Label(self.parent, image=self.category_img, bg=self.bgcolor)
        self.category_label.place(x=300, y=543)
        self.stock_label = tk.Label(self.parent, image=self.stock_img, bg=self.bgcolor)
        self.stock_label.place(x=688, y=547)

        self.tree.bind("<ButtonRelease>", self.tree_on_click)
        self.logout.bind("<Enter>", self.logout_on_hover)
        self.logout.bind("<Button>", self.logout_on_click)
        self.logout.bind("<Leave>", self.logout_off_hover)
        self.search_label.bind("<Button>", self.find_product)
        self.search_label.bind("<Enter>", self.search_on_hover)
        self.search_label.bind("<Leave>", self.search_off_hover)
        self.reset_label.bind("<Enter>", self.resetlabel_on_hover)
        self.reset_label.bind("<Button>", self.resetlabel_on_click)
        self.reset_label.bind("<Leave>", self.resetlabel_off_hover)
        self.remove_label.bind("<Enter>", self.removelabel_on_hover)
        self.remove_label.bind("<Button>", self.removelabel_on_click)
        self.remove_label.bind("<Leave>", self.removelabel_off_hover)
        self.refresh_label.bind("<Enter>", self.refresh_on_hover)
        self.refresh_label.bind("<Button>", self.refresh_on_click)
        self.refresh_label.bind("<Leave>", self.refresh_off_hover)

        self.units = tk.StringVar()
        self.find_strvar = tk.StringVar()
        self.category_strvar = tk.StringVar()
        self.suppliers_strvar = tk.StringVar()
        self.units_cbox = ttk.Combobox(self.parent, width=4, textvariable=self.units)
        self.units_cbox["values"] = ("kg", "pcs", "liters")
        self.units_cbox.place(x=765, y=580)
        self.units_cbox.current(1)

        self.find_cbox = ttk.Combobox(self.parent, width=25, textvariable=self.find_strvar)
        self.find_cbox["values"] = ("ID", "Product Name", "Category", "Supplier")
        self.find_cbox.place(x=570, y=700)
        self.find_cbox.current(1)


        self.suppliers_cbox = ttk.Combobox(self.parent, width=16, textvariable=self.suppliers_strvar)
        self.suppliers_cbox["values"] = self.get_suppliers()
        self.suppliers_cbox.place(x=443, y=580)
        if self.suppliers_strvar != "": self.suppliers_cbox.current(0)

        self.category_cbox = ttk.Combobox(self.parent, width=15, textvariable=self.category_strvar)
        self.category_cbox["values"] = self.get_catdata()
        self.category_cbox.place(x=285, y=580)
        if self.category_strvar != "": self.category_cbox.current(0)

        self.product_entry = ttk.Entry(self.parent, width=22, background=self.bgcolor)
        self.product_entry.place(x=80, y=580)
        self.price_entry = ttk.Entry(self.parent, width=8, background=self.bgcolor)
        self.price_entry.place(x=605, y=580)
        self.stock_entry = ttk.Entry(self.parent, width=8, background=self.bgcolor)
        self.stock_entry.place(x=685, y=580)
        self.find_entry = ttk.Entry(self.parent, width=25, background=self.bgcolor)
        self.find_entry.place(x=570, y=743)
        self.go_etable = tk.Button(self.parent, text="Employees", width=15, height=2,
                                   font=("Arial", 16, "bold"), command=self.goto_etable)
        self.go_etable.config(background=self.bgcolor, highlightthickness=0, highlightbackground=self.bgcolor)
        self.go_etable.bind("<Enter>", self.goetable_on_hover)
        self.go_etable.bind("<Leave>", self.goetable_off_hover)
        self.add_label.bind("<Button>", self.addlabel_on_click)
        self.add_label.bind("<Enter>", self.addlabel_on_hover)
        self.add_label.bind("<Leave>", self.addlabel_off_hover)
        self.go_suptable = tk.Button(self.parent, text="Suppliers", width=15, height=2,
                                     font=("Arial", 16, "bold"), command=self.goto_suptable)
        self.go_suptable.bind("<Enter>", self.go_suptable_on_hover)
        self.go_suptable.bind("<Leave>", self.go_suptable_off_hover)
        self.go_suptable.config(background=self.bgcolor, highlightthickness=0, highlightbackground=self.bgcolor)
        self.go_cattable = tk.Button(self.parent, text="Product Categories", width=15, height=2,
                                     font=("Arial", 16, "bold"), command=self.go_ctable)
        self.go_cattable.config(background=self.bgcolor, highlightthickness=0, highlightbackground=self.bgcolor)
        self.go_cattable.bind("<Enter>", self.gocattable_on_hover)
        self.go_cattable.bind("<Leave>", self.gocattable_off_hover)
        self.uac_button = tk.Button(self.parent, text="Account Settings", width=15, height=2,
                                    font=("Arial", 16, "bold"), command=self.goto_settings)
        self.uac_button.config(background=self.bgcolor, highlightthickness=0, highlightbackground=self.bgcolor)
        self.uac_button.bind("<Enter>", self.uac_on_hover)
        self.uac_button.bind("<Leave>", self.uac_off_hover)
        self.register_sale = tk.Button(self.parent, text="Sales Records", width=15, height=2,
                                    font=("Arial", 16, "bold"), highlightthickness=0,
                                    highlightbackground=self.bgcolor, command=self.registerFrame_init)
        self.register_sale.place(x=195, y=140)
        self.register_sale.bind("<Enter>", self.registersale_on_hover)
        self.register_sale.bind("<Leave>", self.registersale_off_hover)
        self.go_etable.place(x=365, y=140)
        self.go_suptable.place(x=25, y=140)
        self.go_cattable.place(x=705, y=140)
        self.uac_button.place(x=535, y=140)
        self.tree.place(x=78, y=200)
        self.load_products()
        self.stock_count()
        self.update_clock()
        self.dashboard_setup()
        self.get_catdata()
#######
    def logout_off_hover(self, event):
        event.widget.configure(activebackground=self.bgcolor, highlightthickness=0, highlightbackground=self.bgcolor)

    def logout_on_hover(self, event):
        self.logout.configure(highlightthickness=2, highlightbackground="#b4b4b6")

    def logout_on_click(self, event):
        self.logout.configure(highlightthickness=3, highlightbackground="#9d9d9e")
        self.logout_off_hover(event)
        self.mbox = tk.messagebox.askquestion("System", "You are going to be logged out !\n Are you sure?")
        if self.mbox == "yes":
            self.frame.destroy()
            self.app = mainFrame.MainFrame(self.parent)
        else: return

    def addlabel_on_click(self, event):
        self.add_label.configure(highlightthickness=3, highlightbackground="#9d9d9e")
        self.addlabel_off_hover(event)
        self.product = self.product_entry.get()
        self.category = self.category_cbox.get()
        self.supplier = self.suppliers_cbox.get()
        self.stk = self.stock_entry.get()
        self.price = self.price_entry.get()
        self.unit = self.units_cbox.get()
        if self.product == "" or self.category == "" or self.supplier == "":
            return tk.messagebox.showerror("Stock Manager", "You forgot to fill an entry!")
        elif self.stk == "" or self.price == "" or self.unit == "":
            return tk.messagebox.showerror("Stock Manager", "You forgot to fill an entry!")
        if self.updating:
            self.iid = self.tree.focus()
            self.item = self.tree.item(self.iid)
            self.id = self.item["values"][0]
            self.option = tk.messagebox.askquestion("Stock Manager", f"You are going to update the Product ID: {self.id}"
                                                                     f"\nAre you sure?")
            if self.option == "yes":
                self.container = [self.product, self.category, self.supplier, self.price, self.stk, self.unit, self.id]
                self.response = dbHandler.DBHandler.update_product(self, self.container)
                if self.response:
                    tk.messagebox.showinfo("Stock Manager", f"You have succesfully updated Product ID: {self.id}")
                    self.clear_entries()
                    self.clear_focus()
                    self.load_products()
                    self.updating = False
            else: return
        else:
            self.option = tk.messagebox.askquestion("Stock Manager", "You are going to add a new product:\n\n"
                                                                     f"Product Name: {self.product}\n"
                                                                     f"Category: {self.category}\n"
                                                                     f"Supplier: {self.supplier}\n"
                                                                     f"Stock: {self.stk}\n"
                                                                     f"Price: {self.price}\n"
                                                                     f"Unit: {self.unit}\n\nAre you sure?")
            if self.option == "yes":
                self.container = [self.product, self.category, self.supplier, self.stk, self.price, self.unit]
                self.response = dbHandler.DBHandler.add_product(self, self.container)
                if self.response:
                    tk.messagebox.showinfo("Stock Manager", "You've succesfully added a new product !")
                    self.load_products()
                    self.clear_entries()
            else: return

    def addlabel_on_hover(self, event):
        self.add_label.configure(highlightthickness=2, highlightbackground="#b4b4b6")

    def addlabel_off_hover(self, event):
        event.widget.configure(activebackground=self.bgcolor, highlightthickness=0, highlightbackground=self.bgcolor)

    def go_suptable_off_hover(self, event):
        event.widget.configure(activebackground=self.bgcolor, highlightthickness=0, highlightbackground=self.bgcolor)

    def go_suptable_on_hover(self, event):
        self.go_suptable.configure(highlightthickness=0, bg=self.bgcolor, activebackground=self.bgcolor,
                                   highlightbackground="#b4b4b6")
    def uac_off_hover(self, event):
        event.widget.configure(activebackground=self.bgcolor, highlightthickness=0, highlightbackground=self.bgcolor)

    def uac_on_hover(self, event):
        self.uac_button.configure(highlightthickness=0, bg=self.bgcolor, activebackground=self.bgcolor,
                                   highlightbackground="#b4b4b6")
    def goetable_off_hover(self, event):
        event.widget.configure(activebackground=self.bgcolor, highlightthickness=0, highlightbackground=self.bgcolor)

    def goetable_on_hover(self, event):
        self.go_etable.configure(highlightthickness=0, bg=self.bgcolor, activebackground=self.bgcolor,
                                   highlightbackground="#b4b4b6")
    def gocattable_off_hover(self, event):
        event.widget.configure(activebackground=self.bgcolor, highlightthickness=0, highlightbackground=self.bgcolor)

    def gocattable_on_hover(self, event):
        self.go_cattable.configure(highlightthickness=0, bg=self.bgcolor, activebackground=self.bgcolor,
                                   highlightbackground="#b4b4b6")

    def goto_settings(self):
        self.frame.destroy()
        self.app = settingsFrame.SettingsFrame(self.parent, self.user, self.isAdmin, self.emp_id)
    def registersale_off_hover(self, event):
        event.widget.configure(activebackground=self.bgcolor, highlightthickness=0, highlightbackground=self.bgcolor)

    def registersale_on_hover(self, event):
        self.register_sale.configure(highlightthickness=0, bg=self.bgcolor, activebackground=self.bgcolor,
                                   highlightbackground="#b4b4b6")

    def removelabel_off_hover(self, event):
        event.widget.configure(activebackground=self.bgcolor, highlightthickness=0,
                               highlightbackground=self.bgcolor)

    def removelabel_on_click(self, event):
        if self.updating:
            self.iid = self.tree.focus()
            self.item = self.tree.item(self.iid)
            self.id = self.item["values"][0]
            self.option = tk.messagebox.askquestion("Stock Manager", f"You are going to delete Product ID:{self.id}"
                                                                     f"\nAre you sure?")
            if self.option == "yes":
                self.response = dbHandler.DBHandler.remove_product(self, self.id)
                if self.response:
                    self.load_products()
                    self.clear_focus()
                    self.clear_entries()
                    self.updating = False
                    return tk.messagebox.showinfo("Stock Manager", "Product removed succesfully !")
            else: return
        else: return tk.messagebox.showinfo("Stock Manager", "You must select an item first !")

    def removelabel_on_hover(self, event):
        self.remove_label.configure(highlightthickness=2, highlightbackground="#b4b4b6")

    def search_on_hover(self, event):
        self.search_label.configure(highlightthickness=2, highlightbackground="#b4b4b6")

    def search_off_hover(self, event):
        event.widget.configure(activebackground=self.bgcolor, highlightthickness=0, highlightbackground=self.bgcolor)

    def resetlabel_off_hover(self, event):
        event.widget.configure(activebackground=self.bgcolor, highlightthickness=0,
                               highlightbackground=self.bgcolor)

    def resetlabel_on_hover(self,event):
        self.reset_label.configure(highlightthickness=2, highlightbackground="#b4b4b6")

    def resetlabel_on_click(self, event):
        self.updating = False
        self.clear_focus()
        self.clear_entries()

    def dashboard_setup(self):
        """Updates Dashboard Sales and Income Value"""
        self.sales_value = dbHandler.DBHandler.total_sales(self)
        self.sales_intvar.set(self.sales_value[0][0])
        self.value = dbHandler.DBHandler.total_income(self)
        self.income = 0
        for i in self.value:
            self.income += i[0]
        self.income_intvar.set(self.income)

    def update_clock(self):
        """ Live updating the bottom timestamp """
        self.raw_ts = dt.datetime.now(self.timezone)
        self.date_now = self.raw_ts.strftime("%d %b %Y")
        self.time_now = self.raw_ts.strftime("%H:%M:%S %p")
        self.timenow_header.config(text=self.date_now)
        self.today_header.config(text=f" | {self.time_now}")
        self.today_header.after(1000, self.update_clock)

    def focus_iindex(self):
        self.iid = self.tree.focus()
        self.item = self.tree.item(self.iid)
        self.iindex = self.item["values"][0]
        return self.iindex

    def go_ctable(self):
        self.frame.destroy()
        self.app = categoriesFrame.CategoriesFrame(self.parent, self.user, self.isAdmin, self.emp_id)

    def get_catdata(self):
        """Returns category's combobox values from add product section"""
        self.response = dbHandler.DBHandler.get_catdata(self)
        self.values = []
        for i in self.response:
            self.values.append(i[0])
        return tuple(self.values)

    def get_suppliers(self):
        """Returns suppliers's combobox values from add product section"""
        self.response = dbHandler.DBHandler.get_suppliers(self)
        self.values = []
        for i in self.response:
            self.values.append(i[1])
        return tuple(self.values)

    def find_product(self, event):
        self.target = self.find_entry.get()
        self.method = self.find_cbox.get()
        if self.target == "" or self.method == "":
            return tk.messagebox.showerror("System", "You must complete the fields !")
        if self.method == "ID":
            self.method = "product_id"
        elif self.method == "Product Name":
            self.method = "product_name"
        elif self.method == "Category":
            self.method = "category"
        elif self.method == "Supplier":
            self.method = "supplier"
        self.data = dbHandler.DBHandler.search_product(self, self.method, self.target)
        if type(self.data) == None: return tk.messagebox.showinfo("Inventory Manager", "No entries found !")
        else:
            for child in self.tree.get_children():
                self.tree.delete(child)
            self.find_entry.delete(0, tk.END)
            for value in self.data:
                self.tree.insert("", tk.END, values=(value[0], value[1], value[2], value[3], value[4],
                                                     value[5], value[6]))

    def tree_on_click(self, event):
        self.iid = self.tree.focus()
        self.tree.selection_set(self.iid)
        self.updating = True
        self.item = self.tree.item(self.iid)
        self.id = self.item["values"][0]
        self.pname = self.item["values"][1]
        self.category = self.item["values"][2]
        self.supplier = self.item["values"][3]
        self.price = self.item["values"][4]
        self.stock = self.item["values"][5]
        self.unit = self.item["values"][6]
        self.clear_entries()
        self.product_entry.insert(0, self.pname)
        self.category_cbox.insert(0, self.category)
        self.suppliers_cbox.insert(0, self.supplier)
        self.price_entry.insert(0, self.price)
        self.stock_entry.insert(0, self.stock)
        self.units_cbox.insert(0, self.unit)


    def refresh_off_hover(self, event):
        event.widget.configure(activebackground=self.bgcolor, highlightthickness=0, highlightbackground=self.bgcolor)

    def clear_focus(self):
        for i in self.tree.selection():
            self.tree.selection_remove(i)
    def clear_entries(self):
        self.product_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.stock_entry.delete(0, tk.END)
        self.category_cbox.delete(0, tk.END)
        self.suppliers_cbox.delete(0, tk.END)
        self.units_cbox.delete(0, tk.END)
        self.find_entry.delete(0, tk.END)
        self.find_cbox.delete(0, tk.END)

    def refresh_on_hover(self, event):
        self.refresh_label.configure(highlightthickness=2, highlightbackground="#b4b4b6")

    def stock_count(self):
        self.available_stock = dbHandler.DBHandler.stock_count(self)
        return self.available_stock

    def refresh_on_click(self, event):
        self.refresh_label.configure(highlightthickness=3, highlightbackground="#9d9d9e")
        self.refresh_off_hover(event)
        self.load_products()

    def load_products(self):
        for child in self.tree.get_children():
            self.tree.delete(child)
        self.user_products = dbHandler.DBHandler.get_products(self)
        self.rows = dbHandler.DBHandler.get_rowcount(self)
        self.count = 1
        for i in range(len(self.user_products)):
            self.pid = self.user_products[i][0]
            self.pname = self.user_products[i][1],
            self.str = ""
            for item in self.pname:
                self.str += item
            self.name = self.str
            self.pcat = self.user_products[i][2],
            self.supp = (self.user_products[i][3]).strip("{")
            self.stock = self.user_products[i][4],
            self.price = self.user_products[i][5],
            self.unit = self.user_products[i][6]
            self.item = self.tree.insert("", tk.END, values=(self.pid, self.name, self.pcat, self.supp, self.price,
                                                        self.stock, self.unit))
            self.available_stock = self.pid
        self.available_stock = dbHandler.DBHandler.stock_count(self)
        self.stock_intvar.set(self.available_stock)
        self.products_intvar.set(len(self.user_products))
        self.dashboard_setup()

    def goto_suptable(self):
        if self.isAdmin:
            self.frame.destroy()
            self.app = suppliersFrame.SuppliersFrame(self.parent, self.user, self.isAdmin, self.emp_id)

    def goto_etable(self):
        if self.isAdmin:
            self.frame.destroy()
            self.app = empFrame.EmpFrame(self.parent, self.user, self.isAdmin, self.emp_id)
        else: return

    def registerFrame_init(self):
        self.frame.destroy()
        self.app = registerFrame.RegisterFrame(self.parent, self.user, self.isAdmin, self.emp_id)