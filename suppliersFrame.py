import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
import datetime as dt
import pytz
import adminFrame
import credentials
import mainFrame
import dbHandler

class SuppliersFrame():
    """ Initializes Suppliers Frame (only for Admins) """
    def __init__(self, parent, user, isAdmin:bool, emp_id:int):
        self.parent = parent
        self.user = user
        self.isAdmin = isAdmin
        self.emp_id = emp_id
        self.db_params = credentials.connection_params
        self.updating = False
        self.bgcolor = "#ecebeb"
        self.total_supp = 0
        self.timezone = pytz.timezone("Europe/Bucharest")
        self.header = PhotoImage(file="./images/manage_suppliers.png")
        self.invoice = PhotoImage(file="./images/invoice.png")
        self.contact_img = PhotoImage(file="./images/contact.png")
        self.suppname_img = PhotoImage(file="./images/supp_name.png")
        self.suppcontact_img = PhotoImage(file="./images/contact.png")
        self.description_img = PhotoImage(file="./images/description.png")
        self.add_img = PhotoImage(file="./images/add.png")
        self.back_img = PhotoImage(file="./images/back.png")
        self.remove_img = PhotoImage(file="./images/remove.png")
        self.logout_img = PhotoImage(file="./images/logout.png")
        self.logout_label_img = PhotoImage(file="./images/logout_label.png")
        self.totalsupp_img = PhotoImage(file="./images/total_supp.png")
        self.reset_img = PhotoImage(file="./images/undo.png")

        self.GUI()
    def GUI(self):
        self.frame = tk.Frame(self.parent, bg=self.bgcolor, height=900, width=900)
        self.frame.pack()
        self.h_label = tk.Label(self.parent, image=self.header, bg=self.bgcolor)
        self.h_label.place(x=200, y=20)
        self.suppname_label = tk.Label(self.parent, image=self.suppname_img, bg=self.bgcolor)
        self.suppname_label.place(x=70, y=145)
        self.suppname_entry = tk.Entry(self.parent, bg="white", highlightthickness=0, highlightbackground="white",
                                       font=("Arial", 18, "normal"), fg="black")
        self.suppname_entry.place(x=65, y=200)
        self.totalsupp_label = tk.Label(self.parent, image=self.totalsupp_img, bg=self.bgcolor)
        self.totalsupp_label.place(x=420, y=680)
        self.totalsupp_label2 = tk.Label(self.parent, text=self.total_supp, bg=self.bgcolor, fg="#0d92fc",
                                         font=("Arial", 38, "bold"))
        self.totalsupp_label2.place(x=700, y=686)
        self.suppcontact_img = self.suppcontact_img.subsample(2, 2)
        self.suppcontact_label = tk.Label(self.parent, image=self.suppcontact_img, bg=self.bgcolor)
        self.suppcontact_label.place(x=110, y=240)
        self.suppcontact_entry = tk.Entry(self.parent, bg="white", highlightthickness=0, highlightbackground="white",
                                       font=("Arial", 18, "normal"), fg="black")
        self.suppcontact_entry.place(x=65, y=285)
        self.description_img = self.description_img.subsample(2, 2)
        self.description_label = tk.Label(self.parent, image=self.description_img, bg=self.bgcolor)
        self.description_label.place(x=95, y=325)
        self.textbox = tk.Text(self.parent, height=15, width=30, fg="black", bg="white", highlightthickness=0,
                               highlightbackground="white", font=("Arial", 15, "normal"))
        self.textbox.place(x=60, y=370)
        self.add_img = self.add_img.subsample(2, 2)
        self.add_supplier = tk.Label(self.parent, image=self.add_img, bg=self.bgcolor)
        self.add_supplier.place(x=50, y=635)
        self.add_supplier.bind("<Enter>", self.addsup_on_hover)
        self.add_supplier.bind("<Button>", self.addsup_on_click)
        self.add_supplier.bind("<Leave>", self.addsup_off_hover)
        self.remove_img = self.remove_img.subsample(2, 2)
        self.remove_supp = tk.Label(self.parent, image=self.remove_img, bg=self.bgcolor)
        self.remove_supp.place(x=255, y=635)
        self.remove_supp.bind("<Enter>", self.removesupp_on_hover)
        self.remove_supp.bind("<Button>", self.removesupp_on_click)
        self.remove_supp.bind("<Leave>", self.removesupp_off_hover)
        self.back_img = self.back_img.subsample(2, 2)
        self.go_back = tk.Label(self.parent, image=self.back_img, bg=self.bgcolor)
        self.go_back.place(x=50, y=50)
        self.go_back.bind("<Enter>", self.back_on_hover)
        self.go_back.bind("<Button>", self.back_on_click)
        self.go_back.bind("<Leave>", self.back_off_hover)
        self.logout_img = self.logout_img.subsample(2, 2)

        self.logout = tk.Label(self.parent, image=self.logout_img, background=self.bgcolor)
        self.logout.place(x=800, y=55)
        self.logout.bind("<Enter>", self.logout_on_hover)
        self.logout.bind("<Button>", self.logout_on_click)
        self.logout.bind("<Leave>", self.logout_off_hover)
        self.logout_label_img = self.logout_label_img.subsample(2, 2)
        self.logout_label = ttk.Label(self.parent, image=self.logout_label_img, background=self.bgcolor)
        self.logout_label.place(x=780, y=10)
        self.reset_label = tk.Label(self.parent, image=self.reset_img, bg=self.bgcolor)
        self.reset_label.place(x=150, y=635)
        self.reset_label.bind("<Enter>", self.reset_on_hover)
        self.reset_label.bind("<Button>", self.reset_on_click)
        self.reset_label.bind("<Leave>", self.reset_off_hover)

        self.today_header = tk.Label(self.parent, text="", bg=self.bgcolor,
                                     foreground="black", font=("Arial", 14, "italic"))
        self.today_header.place(x=420, y=870)
        self.timenow_header = tk.Label(self.parent, text="", bg=self.bgcolor, foreground="black",
                                       font=("Arial", 14, "italic"))
        self.timenow_header.place(x=337, y=870)

        self.style = ttk.Style(self.parent)
        self.style.theme_use("clam")
        self.style.configure("Treeview", background="white", foreground="black", fieldbackground="white")
        self.tree = ttk.Treeview(self.parent, height=25, columns=4)
        self.tree["columns"] = ("ID", "Name", "Contact", "Description")
        self.tree.column("#0", width=0, minwidth=0)
        self.tree.column("ID", width=35, minwidth=35)
        self.tree.column("Name", width=130, minwidth=90)
        self.tree.column("Contact", width=130, minwidth=90)
        self.tree.column("Description", width=190, minwidth=140)
        self.tree.heading("#0", text="", anchor="w")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Contact", text="Contact")
        self.tree.heading("Description", text="Description")
        self.tree.place(x=350, y=150)
        self.tree.bind("<ButtonRelease>", self.tree_on_click)
        self.update_clock()
        self.load_suppliers()

    def update_clock(self):
        self.raw_ts = dt.datetime.now(self.timezone)
        self.date_now = self.raw_ts.strftime("%d %b %Y")
        self.time_now = self.raw_ts.strftime("%H:%M:%S %p")
        self.timenow_header.config(text=self.date_now)
        self.today_header.config(text=f" | {self.time_now}")
        self.today_header.after(1000, self.update_clock)

    def tree_on_click(self, event):
        self.updating = True
        self.clear_entries()
        self.iid = self.tree.focus()
        self.item = self.tree.item(self.iid)
        self.index = self.item["values"][0]
        self.suppname_entry.insert(0, self.item["values"][1])
        self.suppcontact_entry.insert(0, self.item["values"][2])
        self.textbox.insert(1.0, self.item["values"][3])

    def clear_focus(self):
        for i in self.tree.selection():
            self.tree.selection_remove(i)
    def clear_entries(self):
        self.suppname_entry.delete(0, tk.END)
        self.suppcontact_entry.delete(0, tk.END)
        self.textbox.delete(1.0, tk.END)

    def reset_off_hover(self, event):
        event.widget.configure(activebackground=self.bgcolor, highlightthickness=0, highlightbackground=self.bgcolor)

    def reset_on_click(self, event):
        self.reset_label.configure(highlightthickness=3, highlightbackground="#9d9d9e")
        self.reset_off_hover(event)
        self.clear_focus()
        self.clear_entries()
        self.updating = False

    def reset_on_hover(self, event):
        self.reset_label.configure(highlightthickness=2, highlightbackground="#b4b4b6")

    def addsup_off_hover(self, event):
        event.widget.configure(activebackground=self.bgcolor, highlightthickness=0, highlightbackground=self.bgcolor)
    def addsup_on_hover(self, event):
        self.add_supplier.configure(highlightthickness=2, highlightbackground="#b4b4b6")
    def addsup_on_click(self, event):
        self.add_supplier.configure(highlightthickness=3, highlightbackground="#9d9d9e")
        self.addsup_off_hover(event)
        self.supp_name = self.suppname_entry.get()
        self.supp_contact = self.suppcontact_entry.get()
        self.supp_description = self.textbox.get(1.0, tk.END)
        if self.supp_name == "" or self.supp_contact == "" or len(self.supp_description) < 3:
            return tk.messagebox.showinfo("Stock Manager", "You forgot to fill an entry !")
        if self.updating:
            self.iid = self.tree.focus()
            self.item = self.tree.item(self.iid)
            self.index = self.item["values"][0]
            self.option = tk.messagebox.askquestion("Stock Manager", f"You are going to update Supplier ID:{self.index} !"
                                                                     "\nAre you sure?")
            if self.option == "yes":
                self.container = (self.supp_name, self.supp_contact, self.supp_description, self.index)
                self.response = dbHandler.DBHandler.update_supplier(self, self.container)
                if self.response:
                    self.clear_focus()
                    self.clear_entries()
                    self.load_suppliers()
                    self.updating = False
                    return tk.messagebox.showinfo("Stock Manager", f"You've succesfully updated Supplier ID:{self.index} !")
            else: return
        else:
            self.option = tk.messagebox.askquestion("Stock Manager", "You are going to add a new supplier: \n\n"
                                                                     f"Supplier: {self.supp_name}\n"
                                                                     f"Contact: {self.supp_contact}\n"
                                                                     f"Description: {self.supp_description}\n\n"
                                                                     f"Are you sure?")
            if self.option == "yes":
                self.container = (self.supp_name, self.supp_contact, self.supp_description)
                self.response = dbHandler.DBHandler.add_supplier(self, self.container)
                if self.response:
                    self.clear_entries()
                    self.clear_focus()
                    self.load_suppliers()
                    self.updating = False
                    return tk.messagebox.showinfo("Stock Manager", "You have succesfully added a new supplier !")
            else: return

    def removesupp_off_hover(self, event):
        event.widget.configure(activebackground=self.bgcolor, highlightthickness=0, highlightbackground=self.bgcolor)
    def removesupp_on_hover(self, event):
        self.remove_supp.configure(highlightthickness=2, highlightbackground="#b4b4b6")

    def removesupp_on_click(self, event):
        self.remove_supp.configure(highlightthickness=3, highlightbackground="#9d9d9e")
        self.removesupp_off_hover(event)
        if self.updating:
            self.iid = self.tree.focus()
            self.item = self.tree.item(self.iid)
            self.index = self.item["values"][0]
            self.option = tk.messagebox.askquestion("Stock Manager", f"You are going to remove Supplier ID: {self.index}"
                                                                     f"\nAre you sure?")
            if self.option == "yes":
                self.response = dbHandler.DBHandler.remove_supplier(self, self.index)
                if self.response:
                    self.updating = False
                    self.clear_entries()
                    self.clear_focus()
                    self.load_suppliers()
                    return tk.messagebox.showinfo("Stock Manager", f"You have deleted Supplier ID:{self.index} !")
            else: return
        else: return tk.messagebox.showerror("Stock Manager", "You must select an item !")
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

    def back_off_hover(self, event):
        event.widget.configure(activebackground=self.bgcolor, highlightthickness=0, highlightbackground=self.bgcolor)

    def back_on_hover(self, event):
        self.go_back.configure(highlightthickness=2, highlightbackground="#b4b4b6")

    def back_on_click(self, event):
        self.go_back.configure(highlightthickness=3, highlightbackground="#9d9d9e")
        self.back_off_hover(event)
        self.frame.destroy()
        self.app = adminFrame.AdminFrame(self.parent, self.user, self.isAdmin, self.emp_id)
    def load_suppliers(self):
        for child in self.tree.get_children():
            self.tree.delete(child)
        self.suppliers = dbHandler.DBHandler.get_suppliers(self)
        self.count = 0
        for i in self.suppliers:
            self.count += 1
            self.tree.insert("", tk.END, values=(i[0], i[1], i[2], i[3]))
        self.totalsupp_label2.config(text=self.count)