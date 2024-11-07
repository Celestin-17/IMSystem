import tkinter as tk
from tkinter import PhotoImage
from tkinter import ttk
import datetime as dt
import pytz
import categoriesFrame
import credentials
import mainFrame
import dbHandler
import registerFrame
import settingsFrame


class UserFrame():
    """ Initializes Employees Dashboard Frame (only for Employees) """
    def __init__(self, parent, user, isAdmin:bool, emp_id:int):
        self.parent = parent
        self.user = user
        self.isAdmin = isAdmin
        self.emp_id = emp_id
        self.db_params = credentials.connection_params
        self.income_intvar = tk.IntVar()
        self.emp_totalsales_intvar = tk.IntVar()
        self.generated_revenue_intvar = tk.IntVar()
        self.available_stock_intvar = tk.IntVar()
        self.total_products_intvar = tk.IntVar()
        self.bgcolor = "#ecebeb"
        self.updating = False
        self.timezone = pytz.timezone("Europe/Bucharest")
        self.title_img = PhotoImage(file="./images/admin_dboard.png")
        self.passlabel_img = PhotoImage(file="./images/passlabel_img.png")
        self.userlabel_img = PhotoImage(file="./images/userlabel_img.png")
        self.title2_img = PhotoImage(file="./images/user.png")
        self.login_button_img = PhotoImage(file="./images/arrow.png")
        self.stock_heading = PhotoImage(file="./images/emp_dboard.png")
        self.refresh_img = PhotoImage(file="./images/refresh.png")
        self.logout_img = PhotoImage(file="./images/logout.png")
        self.logout_label_img = PhotoImage(file="./images/logout_label.png")
        self.reset_img = PhotoImage(file="./images/undo.png")
        self.findby_img = PhotoImage(file="./images/findby.png")
        self.search_img = PhotoImage(file="./images/search.png")
        self.GUI()


    def GUI(self):
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
        self.total_products_label = tk.Label(self.parent, text="Products in stock: ", bg=self.bgcolor, fg="black",
                                             font=("Arial", 20, "bold"))
        self.total_products_label.place(x=140, y=650)
        self.availablestock_label = tk.Label(self.parent, text="Available stock: ", bg=self.bgcolor, fg="black",
                                             font=("Arial", 20, "bold"))
        self.availablestock_label.place(x=140, y=690)
        self.total_label = tk.Label(self.parent, font=("Arial", 20, "bold"), bg=self.bgcolor, fg="blue",
                                    textvariable=self.total_products_intvar)
        self.total_label.place(x=320, y=650)
        self.stock_label2 = tk.Label(self.parent, font=("Arial", 20, "bold"), bg=self.bgcolor, fg="blue",
                                     textvariable=self.available_stock_intvar)
        self.stock_label2.place(x=305, y=690)
        self.total_sales = tk.Label(self.parent, text=f"Sales you recorded:", font=("Arial", 20, "bold"), bg=self.bgcolor,
                                    fg="black")
        self.total_sales.place(x=140, y=730)
        self.sales_label = tk.Label(self.parent, textvariable=self.emp_totalsales_intvar, font=("Arial", 20, "bold"),
                                    bg=self.bgcolor, fg="blue")
        self.sales_label.place(x=340, y=730)
        self.generated_income_label = tk.Label(self.parent, text="Generated income: ", fg="black", bg=self.bgcolor,
                                               font=("Arial", 20, "bold"))
        self.generated_income_label.place(x=140, y=770)
        self.generated_revenue_label = tk.Label(self.parent, textvariable=self.generated_revenue_intvar, fg="blue",
                                                bg=self.bgcolor, font=("Arial", 20, "bold"))
        self.generated_revenue_label.place(x=330, y=770)
        self.empid_label = tk.Label(self.parent, text=f"(Employee ID: {self.emp_id})", bg=self.bgcolor, fg="black",
                                    font=("Arial", 16, "bold"))
        self.empid_label.place(x=190, y=600)
        self.welcome_label = tk.Label(self.parent, text=f"Welcome back, {self.user} ! ", font=("Arial", 25, "italic"),
                                       background=self.bgcolor, bg=self.bgcolor, fg="black")
        self.welcome_label.place(x=120, y=560)

        ### Live timestamp setup

        self.today_header = tk.Label(self.parent, text="", bg=self.bgcolor, foreground="black", font=("Arial", 14, "italic"))
        self.today_header.place(x=420, y=875)
        self.timenow_header = tk.Label(self.parent, text="", bg=self.bgcolor, foreground="black",
                                       font=("Arial", 14, "italic"))
        self.timenow_header.place(x=337, y=875)
        self.logout_img = self.logout_img.subsample(2, 2)
        self.logout = tk.Label(self.parent, image=self.logout_img, background=self.bgcolor)
        self.logout.place(x=810, y=55)
        self.logout_label_img = self.logout_label_img.subsample(2, 2)
        self.logout_label = ttk.Label(self.parent, image=self.logout_label_img, background=self.bgcolor)
        self.logout_label.place(x=783, y=10)
        self.findby_label = tk.Label(self.parent, image=self.findby_img, bg=self.bgcolor)
        self.findby_label.place(x=500, y=550)
        self.search_img = self.search_img.subsample(2, 2)
        self.search_label = tk.Label(self.parent, image=self.search_img, bg=self.bgcolor)
        self.search_label.place(x=610, y=730)

        self.tree.bind("<ButtonRelease>", self.tree_on_click)
        self.logout.bind("<Enter>", self.logout_on_hover)
        self.logout.bind("<Button>", self.logout_on_click)
        self.logout.bind("<Leave>", self.logout_off_hover)
        self.search_label.bind("<Button>", self.find_product)
        self.search_label.bind("<Enter>", self.search_on_hover)
        self.search_label.bind("<Leave>", self.search_off_hover)
        self.refresh_label.bind("<Enter>", self.refresh_on_hover)
        self.refresh_label.bind("<Button>", self.refresh_on_click)
        self.refresh_label.bind("<Leave>", self.refresh_off_hover)

        self.find_strvar = tk.StringVar()
        self.find_cbox = ttk.Combobox(self.parent, width=25, textvariable=self.find_strvar)
        self.find_cbox["values"] = ("ID", "Product Name", "Category", "Supplier")
        self.find_cbox.place(x=530, y=630)
        self.find_cbox.current(1)
        self.find_entry = ttk.Entry(self.parent, width=25, background=self.bgcolor)
        self.find_entry.place(x=530, y=680)

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
        self.uac_button.place(x=535, y=140)
        self.tree.place(x=78, y=200)
        self.load_products()
        self.stock_count()
        self.update_clock()
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

    # def addlabel_on_click(self, event):
    #     self.add_label.configure(highlightthickness=3, highlightbackground="#9d9d9e")
    #     self.addlabel_off_hover(event)
    #     self.product = self.product_entry.get()
    #     self.category = self.category_cbox.get()
    #     self.supplier = self.suppliers_cbox.get()
    #     self.stk = self.stock_entry.get()
    #     self.price = self.price_entry.get()
    #     self.unit = self.units_cbox.get()
    #     if self.product == "" or self.category == "" or self.supplier == "":
    #         return tk.messagebox.showerror("Stock Manager", "You forgot to fill an entry!")
    #     elif self.stk == "" or self.price == "" or self.unit == "":
    #         return tk.messagebox.showerror("Stock Manager", "You forgot to fill an entry!")
    #     if self.updating:
    #         self.iid = self.tree.focus()
    #         self.item = self.tree.item(self.iid)
    #         self.id = self.item["values"][0]
    #         self.option = tk.messagebox.askquestion("Stock Manager", f"You are going to update the Product ID: {self.id}"
    #                                                                  f"\nAre you sure?")
    #         if self.option == "yes":
    #             self.container = [self.product, self.category, self.supplier, self.price, self.stk, self.unit, self.id]
    #             self.response = dbHandler.DBHandler.update_product(self, self.container)
    #             if self.response:
    #                 tk.messagebox.showinfo("Stock Manager", f"You have succesfully updated Product ID: {self.id}")
    #                 self.clear_entries()
    #                 self.clear_focus()
    #                 self.load_products()
    #                 self.updating = False
    #         else: return
    #     else:
    #         self.option = tk.messagebox.askquestion("Stock Manager", "You are going to add a new product:\n\n"
    #                                                                  f"Product Name: {self.product}\n"
    #                                                                  f"Category: {self.category}\n"
    #                                                                  f"Supplier: {self.supplier}\n"
    #                                                                  f"Stock: {self.stk}\n"
    #                                                                  f"Price: {self.price}\n"
    #                                                                  f"Unit: {self.unit}\n\nAre you sure?")
    #         if self.option == "yes":
    #             self.container = [self.product, self.category, self.supplier, self.stk, self.price, self.unit]
    #             self.response = dbHandler.DBHandler.add_product(self, self.container)
    #             if self.response:
    #                 tk.messagebox.showinfo("Stock Manager", "You've succesfully added a new product !")
    #                 self.load_products()
    #                 self.clear_entries()
    #         else: return

    # def addlabel_on_hover(self, event):
    #     self.add_label.configure(highlightthickness=2, highlightbackground="#b4b4b6")
    #
    # def addlabel_off_hover(self, event):
    #     event.widget.configure(activebackground=self.bgcolor, highlightthickness=0, highlightbackground=self.bgcolor)

    # def go_suptable_off_hover(self, event):
    #     event.widget.configure(activebackground=self.bgcolor, highlightthickness=0, highlightbackground=self.bgcolor)
    #
    # def go_suptable_on_hover(self, event):
    #     self.go_suptable.configure(highlightthickness=0, bg=self.bgcolor, activebackground=self.bgcolor,
    #                                highlightbackground="#b4b4b6")
    def uac_off_hover(self, event):
        event.widget.configure(activebackground=self.bgcolor, highlightthickness=0, highlightbackground=self.bgcolor)

    def uac_on_hover(self, event):
        self.uac_button.configure(highlightthickness=0, bg=self.bgcolor, activebackground=self.bgcolor,
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

    # def removelabel_on_click(self, event):
    #     if self.updating:
    #         self.iid = self.tree.focus()
    #         self.item = self.tree.item(self.iid)
    #         self.id = self.item["values"][0]
    #         self.option = tk.messagebox.askquestion("Stock Manager", f"You are going to delete Product ID:{self.id}"
    #                                                                  f"\nAre you sure?")
    #         if self.option == "yes":
    #             self.response = dbHandler.DBHandler.remove_product(self, self.id)
    #             if self.response:
    #                 self.load_products()
    #                 self.clear_entries()
    #                 self.clear_focus()
    #                 self.updating = False
    #                 return tk.messagebox.showinfo("Stock Manager", "Product removed succesfully !")
    #         else: return
    #     else: return tk.messagebox.showinfo("Stock Manager", "You must select an item first !")
    # def removelabel_on_hover(self, event):
    #     self.remove_label.configure(highlightthickness=2, highlightbackground="#b4b4b6")

    def search_on_hover(self, event):
        self.search_label.configure(highlightthickness=2, highlightbackground="#b4b4b6")

    def search_off_hover(self, event):
        event.widget.configure(activebackground=self.bgcolor, highlightthickness=0, highlightbackground=self.bgcolor)
    #
    # def resetlabel_off_hover(self, event):
    #     event.widget.configure(activebackground=self.bgcolor, highlightthickness=0,
    #                            highlightbackground=self.bgcolor)
    #
    # def resetlabel_on_hover(self,event):
    #     self.reset_label.configure(highlightthickness=2, highlightbackground="#b4b4b6")
    #
    # def resetlabel_on_click(self, event):
    #     self.updating = False
    #     self.clear_focus()
    #     self.clear_entries()


    def update_clock(self):
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


    # def remove_on_click(self):
    #     self.value = self.remove_entry.get()
    #     if self.value == "":
    #         self.iid = self.tree.focus()
    #         self.item = self.tree.item(self.iid)
    #         self.index = self.item["values"][0]
    #
    #         dbHandler.DBHandler.remove_product(self, self.index)
    #         self.tree.delete(self.iid)
    #         self.clear_entries()
    #         self.load_products()
    #     else:
    #         for child in self.tree.get_children():
    #             self.index = self.tree.item(child)["values"][0]
    #             if int(self.value) == self.index:
    #                 self.mbox = tk.messagebox.askquestion("System", f"Are you sure to destroy the record with index:{self.index}")
    #                 if self.mbox == "no":
    #                     self.clear_entries()
    #                     return
    #                 else:
    #                     self.tree.delete(child)
    #                     dbHandler.DBHandler.remove_product(self, self.index)
    #                     self.clear_entries()
    #                     self.load_products()
    #                     return

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
        if type(self.data) == None: return
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
    def refresh_off_hover(self, event):
        event.widget.configure(activebackground=self.bgcolor, highlightthickness=0, highlightbackground=self.bgcolor)

    def clear_focus(self):   # Clears treeview focus
        for i in self.tree.selection():
            self.tree.selection_remove(i)

    def get_revenue(self):
        """ Returns emp_id's generated revenue """
        self.response = dbHandler.DBHandler.generated_revenue(self, self.emp_id)
        self.revenue = 0
        for i in self.response:
            self.revenue += i[0]
        return self.revenue
    def clear_entries(self):
        self.find_entry.delete(0, tk.END)
        self.find_cbox.delete(0, tk.END)

    def refresh_on_hover(self, event):
        self.refresh_label.configure(highlightthickness=2, highlightbackground="#b4b4b6")

    def stock_count(self):
        self.available_stock = dbHandler.DBHandler.stock_count(self)
        self.available_stock_intvar.set(self.available_stock)
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
        self.available_stock = dbHandler.DBHandler.stock_count(self)
        self.available_stock_intvar.set(self.available_stock)
        self.total_products_intvar.set(len(self.user_products))

        self.emp_totalsales = dbHandler.DBHandler.get_empsales(self, self.emp_id)
        self.generated_revenue = self.get_revenue()
        self.generated_revenue_intvar.set(self.generated_revenue)
        self.emp_totalsales_intvar.set(self.emp_totalsales[0][0])

    def registerFrame_init(self):
        self.frame.destroy()
        self.app = registerFrame.RegisterFrame(self.parent, self.user, self.isAdmin, self.emp_id)