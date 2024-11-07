import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
import adminFrame
import pytz
import datetime as dt
import credentials
import dbHandler
import mainFrame
import userFrame


class EmpFrame():
    """ Initializes Employees Frame (only for Admins) """
    def __init__(self, parent, user, isAdmin:bool, emp_id:int):
        self.parent = parent
        self.user = user
        self.isAdmin = isAdmin
        self.emp_id = emp_id
        self.db_params = credentials.connection_params
        self.bgcolor = "#ecebeb"
        self.updating = False
        self.timezone = pytz.timezone("Europe/Bucharest")
        self.header = PhotoImage(file="./images/emp_header.png")
        self.name_img = PhotoImage(file="./images/name.png")
        self.pass_img = PhotoImage(file="./images/pass_2.png")
        self.email_img = PhotoImage(file="./images/eemail.png")
        self.gender_img = PhotoImage(file="./images/gender.png")
        self.dob_img = PhotoImage(file="./images/dob.png")
        self.contact_img = PhotoImage(file="./images/contact.png")
        self.emptype_img = PhotoImage(file="./images/emptype.png")
        self.salary_img = PhotoImage(file="./images/salary.png")
        self.address_img = PhotoImage(file="./images/address.png")
        self.usertype_img = PhotoImage(file="./images/user_type.png")
        self.add_img = PhotoImage(file="./images/add.png")
        self.remove_img = PhotoImage(file="./images/remove.png")
        self.refresh_img = PhotoImage(file="./images/refresh_2.png")
        self.logout_img = PhotoImage(file="./images/logout.png")
        self.back_img = PhotoImage(file="./images/back.png")
        self.logout_label_img = PhotoImage(file="./images/logout_label.png")
        self.totalemp_img = PhotoImage(file="./images/total_emp.png")
        self.reset_img = PhotoImage(file="./images/undo.png")
        self.today = dt.datetime.today()
        self.day = self.today.day
        self.month = self.today.month
        self.year = self.today.year
        self.GUI()

    def GUI(self):
        self.frame = tk.Frame(self.parent, width=1000, height=900, bg=self.bgcolor)
        self.frame.pack()
        self.header_label = tk.Label(self.parent, image=self.header, bg=self.bgcolor)
        self.header_label.place(x=140, y=-10)

        self.style = ttk.Style(self.parent)
        self.style.theme_use("clam")
        self.tree = ttk.Treeview(height=17, columns=12)
        self.tree.place(x=15, y=130)

        self.style.configure("Treeview", background="white", foreground="black", fieldbackground="white")
        self.tree["columns"] = ("EmpID", "Name", "Password", "Email", "Gender", "Birthday", "Contact",
                                "Salary", "EmpType", "Address", "UserType")
        self.tree.column("#0", width=0, minwidth=0)
        self.tree.column("EmpID", width=40, minwidth=50)
        self.tree.column("Name", width=100, minwidth=65)
        self.tree.column("Password", width=100, minwidth=65)
        self.tree.column("Email", width=100, minwidth=65)
        self.tree.column("Gender", width=55, minwidth=55)
        self.tree.column("Birthday", width=100, minwidth=65)
        self.tree.column("Contact", width=100, minwidth=65)
        self.tree.column("Salary", width=80, minwidth=80)
        self.tree.column("EmpType", width=100, minwidth=65)
        self.tree.column("Address", width=100, minwidth=65)
        self.tree.column("UserType", width=90, minwidth=65)

        self.tree.heading("#0", text="Label", anchor="w")
        self.tree.heading("EmpID", text="EmpID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Password", text="Password")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Gender", text="Gender")
        self.tree.heading("Birthday", text="Birthday")
        self.tree.heading("Contact", text="Contact")
        self.tree.heading("Salary", text="Salary")
        self.tree.heading("EmpType", text="EmpType")
        self.tree.heading("Address", text="Address")
        self.tree.heading("UserType", text="UserType")

        self.name_label = tk.Label(self.parent, image=self.name_img, bg=self.bgcolor)
        self.name_label.place(x=30, y=550)
        self.pass_label = tk.Label(self.parent, image=self.pass_img, bg=self.bgcolor)
        self.pass_label.place(x=30, y=600)
        self.email_label = tk.Label(self.parent, image=self.email_img, bg=self.bgcolor)
        self.email_label.place(x=30, y=650)
        self.gender_label = tk.Label(self.parent, image=self.gender_img, bg=self.bgcolor)
        self.gender_label.place(x=30, y=700)
        self.dob_label = tk.Label(self.parent, image=self.dob_img, bg=self.bgcolor)
        self.dob_label.place(x=30, y=750)
        self.contact_img = self.contact_img.subsample(2, 2)
        self.contact_label = tk.Label(self.parent, image=self.contact_img, bg=self.bgcolor)
        self.contact_label.place(x=30, y=800)
        self.emptype_label = tk.Label(self.parent, image=self.emptype_img, bg=self.bgcolor)
        self.emptype_label.place(x=490, y=545)
        self.salary_label = tk.Label(self.parent, image=self.salary_img, bg=self.bgcolor)
        self.salary_label.place(x=495, y=600)
        self.address_label = tk.Label(self.parent, image=self.address_img, bg=self.bgcolor)
        self.address_label.place(x=490, y=700)
        self.usertype_label = tk.Label(self.parent, image=self.usertype_img, bg=self.bgcolor)
        self.usertype_label.place(x=490, y=650)
        self.add_img = self.add_img.subsample(2, 2)
        self.add_entry = tk.Label(self.parent, image=self.add_img, bg=self.bgcolor)
        self.add_entry.place(x=590, y=840)
        self.add_entry.bind("<Enter>", self.addlabel_on_hover)
        self.add_entry.bind("<Button>", self.addlabel_on_click)
        self.add_entry.bind("<Leave>", self.addlabel_off_hover)
        self.tree.bind("<ButtonRelease>", self.tree_on_click)
        self.remove_img = self.remove_img.subsample(2, 2)
        self.remove_entry = tk.Label(self.parent, image=self.remove_img, bg=self.bgcolor)
        self.remove_entry.place(x=730, y=840)
        self.remove_entry.bind("<Enter>", self.remove_entry_on_hover)
        self.remove_entry.bind("<Button>", self.remove_entry_on_click)
        self.remove_entry.bind("<Leave>", self.remove_entry_off_hover)
        self.refresh_label = tk.Label(self.parent, image=self.reset_img, bg=self.bgcolor)
        self.refresh_label.place(x=855, y=837)
        self.refresh_label.bind("<Enter>", self.refresh_label_on_hover)
        self.refresh_label.bind("<Button>", self.refresh_label_on_click)
        self.refresh_label.bind("<Leave>", self.refresh_label_off_hover)
        self.logout_img = self.logout_img.subsample(2, 2)
        self.logout = tk.Label(self.parent, image=self.logout_img, background=self.bgcolor)
        self.logout.place(x=894, y=47)
        self.logout_label_img = self.logout_label_img.subsample(2, 2)
        self.logout_label = ttk.Label(self.parent, image=self.logout_label_img, background=self.bgcolor)
        self.logout_label.place(x=870, y=8)
        self.logout.bind("<Enter>", self.logout_on_hover)
        self.logout.bind("<Button>", self.logout_on_click)
        self.logout.bind("<Leave>", self.logout_off_hover)
        self.totalemp_label = tk.Label(self.parent, image=self.totalemp_img, bg=self.bgcolor)
        self.totalemp_label.place(x=23, y=500)
        self.totalemp = tk.IntVar(self.parent)
        self.totalemp_nr = tk.Label(self.parent, textvariable=self.totalemp, fg="#0d92fc",
                                    bg=self.bgcolor, font=("Arial", 30, "bold"))
        self.totalemp_nr.place(x=275, y=507)
        self.today_header = tk.Label(self.parent, text="", bg=self.bgcolor,
                                     foreground="black", font=("Arial", 14, "italic"))
        self.today_header.place(x=420, y=875)
        self.timenow_header = tk.Label(self.parent, text="", bg=self.bgcolor, foreground="black",
                                       font=("Arial", 14, "italic"))
        self.timenow_header.place(x=337, y=875)
        self.back_img = self.back_img.subsample(2, 2)
        self.go_back = tk.Label(self.parent, image=self.back_img, bg=self.bgcolor)
        self.go_back.place(x=30, y=20)
        self.go_back.bind("<Enter>", self.goback_on_hover)
        self.go_back.bind("<Button>", self.goback_on_click)
        self.go_back.bind("<Leave>", self.goback_off_hover)

        self.prefix_strvar = tk.StringVar(self.parent)
        self.prefix_cbox = ttk.Combobox(self.parent, width=5, textvariable=self.prefix_strvar)
        self.prefix_cbox["values"] = ("(+39)", "(+40)", "(+46)", "(+47)", "(+48)", "(+49)", "(+54)")
        self.prefix_cbox.current(1)
        self.prefix_cbox.place(x=160, y=810)

        self.name_entry = tk.Entry(self.parent, width=25, bg="white", highlightthickness=0, fg="black",
                                   font=("Arial", 15, "normal"))
        self.name_entry.place(x=230, y=560)
        self.pass_entry = tk.Entry(self.parent, width=25, bg="white", highlightthickness=0, fg="black",
                                   font=("Arial", 15, "normal"))
        self.pass_entry.place(x=230, y=610)
        self.email_entry = tk.Entry(self.parent, width=25, bg="white", highlightthickness=0, fg="black",
                                    font=("Arial", 15, "normal"))
        self.email_entry.place(x=230, y=660)
        self.gender_strvar = tk.StringVar(self.parent)
        self.gender_cbox = ttk.Combobox(self.parent, width=25, textvariable=self.gender_strvar, font=("Arial", 15, "normal"))
        self.gender_cbox["values"] = ("Male", "Female")
        self.gender_cbox.current(0)
        self.gender_cbox.place(x=230, y=710)

        self.date_entry = tk.Entry(self.parent, width=25, bg="white", highlightthickness=0, fg="black")
        self.date_entry.place(x=230, y=760)
        self.date_entry.insert(0, "YYYY-MM-DD")
        self.date_entry.bind("<Button>", self.dentry_on_click)
        self.date_entry.bind("<Leave>", self.dentry_off_hover)

        self.contact_entry = tk.Entry(self.parent, width=25, bg="white", highlightthickness=0, fg="black",
                                      font=("Arial", 15, "italic"))
        self.contact_entry.place(x=230, y=810)

        self.emp_type = tk.StringVar(self.parent)
        self.emptype_cbox = ttk.Combobox(self.parent, width=20, textvariable=self.emp_type,
                                         font=("Arial", 15, "normal"))
        self.emptype_cbox["values"] = ("full-time", "part-time")
        self.emptype_cbox.current(0)
        self.emptype_cbox.place(x=730, y=560)

        self.usertype_strvar = tk.StringVar(self.parent)
        self.usertype_cbox = ttk.Combobox(self.parent, width=27, textvariable=self.usertype_strvar,
                                         font=("Arial", 15, "normal"))
        self.usertype_cbox["values"] = ("Employee", "Admin")
        self.usertype_cbox.current(0)
        self.usertype_cbox.place(x=630, y=660)
        self.salary_entry = tk.Entry(self.parent, width=27, bg="white", highlightthickness=0, fg="black",
                                     font=("Arial", 15, "normal"))
        self.salary_entry.place(x=630, y=610)
        self.address_entry = tk.Text(self.parent, width=35, height=7, background="white", fg="black",
                                     highlightthickness=0, font=("Arial", 15, "normal"))
        self.address_entry.place(x=630, y=710)
        self.update_clock()
        self.load_tree()

    def get_timestamp(self):
        self.timestamp = dt.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        return self.timestamp

    def clear_entries(self):
        for i in self.tree.selection():
            self.tree.selection_remove(i)
        self.updating = False
        self.name_entry.delete(0, tk.END)
        self.pass_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.gender_cbox.delete(0, tk.END)
        self.prefix_cbox.delete(0, tk.END)
        self.emptype_cbox.delete(0, tk.END)
        self.contact_entry.delete(0, tk.END)
        self.usertype_cbox.delete(0, tk.END)
        self.salary_entry.delete(0, tk.END)
        self.address_entry.delete(1.0, tk.END)
        self.date_entry.delete(0, tk.END)

    def update_clock(self):
        self.raw_ts = dt.datetime.now(self.timezone)
        self.date_now = self.raw_ts.strftime("%d %b %Y")
        self.time_now = self.raw_ts.strftime("%H:%M:%S %p")
        self.timenow_header.config(text=self.date_now)
        self.today_header.config(text=f" | {self.time_now}")
        self.today_header.after(1000, self.update_clock)

    def goback_off_hover(self, event):
        event.widget.configure(activebackground=self.bgcolor, highlightthickness=0, highlightbackground=self.bgcolor)

    def goback_on_hover(self, event):
        self.go_back.configure(highlightthickness=2, highlightbackground="#b4b4b6")

    def goback_on_click(self, event):
        self.go_back.configure(highlightthickness=3, highlightbackground="#9d9d9e")
        self.goback_off_hover(event)
        # self.mbox = tk.messagebox.askquestion("System", "You are going to be logged out !\n Are you sure?")
        # if self.mbox == "yes":
        if self.isAdmin:
            self.frame.destroy()
            self.app = adminFrame.AdminFrame(self.parent, self.user, self.isAdmin, self.emp_id)
        else:
            self.frame.destroy()
            self.app = userFrame.UserFrame(self.parent, self.user, self.isAdmin, self.emp_id)

    def load_tree(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        self.employees = dbHandler.DBHandler.load_emptree(self)
        self.count = 0
        for i in self.employees:
            self.count += 1
            self.tree.insert("", tk.END, values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6],
                                                 i[7], i[8], i[9], i[10]))
        self.totalemp.set(self.count)

    def tree_on_click(self, event):
        self.clear_entries()
        self.iid = self.tree.focus()
        self.tree.selection_set(self.iid)
        self.updating = True
        self.item = self.tree.item(self.iid)
        self.emp_id = self.item["values"][0]
        self.emp_name = self.item["values"][1]
        self.pwd = self.item["values"][2]
        self.email = self.item["values"][3]
        self.gender = self.item["values"][4]
        self.birthday = self.item["values"][5]
        self.contact = self.item["values"][6]
        self.salary = self.item["values"][7]
        self.workshift = self.item["values"][8]
        self.address = self.item["values"][9]
        self.usertype = self.item["values"][10]
        self.name_entry.insert(0, self.emp_name)
        self.pass_entry.insert(0, self.pwd)
        self.email_entry.insert(0, self.email)
        self.gender_cbox.insert(0, self.gender)
        self.date_entry.insert(0, self.birthday)
        self.prefix = f"+{str(self.contact)[:2]}"
        self.contact = str(self.contact)[2:]
        self.contact_entry.insert(0, self.contact)
        self.prefix = self.prefix_cbox.insert(0, self.prefix)
        self.salary_entry.insert(0, self.salary)
        self.emptype_cbox.insert(0, self.workshift)
        self.address_entry.insert(1.0, self.address)
        self.usertype_cbox.insert(0, self.usertype)

    def dentry_on_click(self, event):
        self.date_entry.delete(0, tk.END)

    def dentry_off_hover(self, event):
        if self.date_entry.get() == "":
            self.date_entry.delete(0, tk.END)
            self.date_entry.insert(0, "YYYY-MM-DD")

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

    def addlabel_off_hover(self, event):
        event.widget.configure(activebackground=self.bgcolor, highlightthickness=0, highlightbackground=self.bgcolor)

    def addlabel_on_hover(self, event):
        self.add_entry.configure(highlightthickness=2, highlightbackground="#b4b4b6")

    def addlabel_on_click(self, event):
        self.add_entry.configure(highlightthickness=3, highlightbackground="#9d9d9e")
        self.addlabel_off_hover(event)
        self.timestamp = self.get_timestamp()
        self.name = self.name_entry.get()
        self.password = self.pass_entry.get()
        self.email = self.email_entry.get()
        self.gender = self.gender_cbox.get()
        self.birthday = self.date_entry.get()
        self.prefix = self.prefix_cbox.get()
        self.phone = self.contact_entry.get()
        self.emptype = str(self.emptype_cbox.get())
        self.salary = self.salary_entry.get()
        self.usertype = self.usertype_cbox.get()
        self.address = self.address_entry.get(1.0, tk.END)

        self.contact = f"{self.prefix[1:4]}{self.phone[:11]}"

        if self.name == "" or self.password == "" or self.email == "" or self.gender == "" or self.birthday == "":
            return tk.messagebox.showerror("Stock Manager", "You forgot to fill an entry !")
        elif self.prefix == "" or self.phone == "" or self.emptype == "" or len(self.address) < 3:
            return tk.messagebox.showerror("Stock Manager", "You forgot to fill an entry !")
        elif self.salary == "" or self.usertype == "":
            return tk.messagebox.showerror("Stock Manager", "You forgot to fill an entry !")
        if self.updating:
            self.iid = self.tree.focus()
            self.tree.selection_set(self.iid)
            self.item = self.tree.item(self.iid)
            self.emp_id = self.item["values"][0]
            self.container = [self.name, self.password, self.email, self.gender, self.birthday, self.contact, self.salary,
                           self.emptype, self.address, self.usertype, self.emp_id]
            self.option = tk.messagebox.askquestion("Stock Manager", "You are going to update the details of Employee "
                                                                     f"ID:{self.emp_id} !\n\n"
                                                                     f"Name: {self.name}\n"
                                                                     f"Password: {self.password}\n"
                                                                     f"Email: {self.email}\n"
                                                                     f"Gender: {self.birthday}\n"
                                                                     f"Date of birth: {self.birthday}\n"
                                                                     f"Phone: {self.contact}\n"
                                                                     f"Salary: {self.salary} $\n"
                                                                     f"Employment type: {self.emptype}\n"
                                                                     f"Address: {self.address}\n"
                                                                     f"User Acces Level: {self.usertype}\n\n"
                                                                     f"Are you sure?")
            if self.option == "yes":
                self.response = dbHandler.DBHandler.update_employee(self, self.container)
                if self.response:
                    tk.messagebox.showinfo("Stock Manager", "Updated succesfully !")
                    self.clear_entries()
                    self.load_tree()
                    return
                else: return                (name, password, email, gender, birthday, contact,
                                                salary, workshift, address, usertype)
            else: return
        else:
            self.timestamp = self.get_timestamp()
            self.container = [self.name, self.password, self.email, self.gender, self.birthday, self.contact,
            self.salary, self.emptype, self.address, self.usertype]
            self.option = tk.messagebox.askquestion("Stock Manager", "You are going to add a new employee:\n\n"
                                                                     f"Name: {self.name}\n"
                                                                     f"Password: {self.password}\n"
                                                                     f"Email: {self.email}\n"
                                                                     f"Gender: {self.birthday}\n"
                                                                     f"Date of birth: {self.birthday}\n"
                                                                     f"Phone: {self.contact}\n"
                                                                     f"Salary: {self.salary} $\n"
                                                                     f"Employment type: {self.emptype}\n"
                                                                     f"Address: {self.address}\n"
                                                                     f"User Acces Level: {self.usertype}\n\n"
                                                                     "Are you sure?")
            if self.option == "yes":
                self.emp_id = dbHandler.DBHandler.add_employee(self, self.container)
                if self.response:
                    self.clear_entries()
                    self.load_tree()
                    return tk.messagebox.showinfo("Stock Manager", f"You have succesfully added Employee ID:{self.emp_id}")
                else: return

    def remove_entry_off_hover(self, event):
        event.widget.configure(activebackground=self.bgcolor, highlightthickness=0, highlightbackground=self.bgcolor)

    def remove_entry_on_hover(self, event):
        self.remove_entry.configure(highlightthickness=2, highlightbackground="#b4b4b6")

    def remove_entry_on_click(self, event):
        self.remove_entry.configure(highlightthickness=3, highlightbackground="#9d9d9e")
        self.remove_entry_off_hover(event)
        if self.updating:
            self.iid = self.tree.focus()
            self.item = self.tree.item(self.iid)
            self.id = self.item["values"][0]
            self.option = tk.messagebox.askquestion("Stock Manager", f"You are going to remove Employee ID:{self.id}\n"
                                                                     "Are you sure?")
            if self.option == "yes":
                self.response = dbHandler.DBHandler.remove_employee(self, self.id)
                if self.response:
                    self.load_tree()
                    return tk.messagebox.showinfo("Stock Manager", f"You have removed Employee ID: {self.id}")

    def refresh_label_off_hover(self, event):
        event.widget.configure(activebackground=self.bgcolor, highlightthickness=0, highlightbackground=self.bgcolor)

    def refresh_label_on_hover(self, event):
        self.refresh_label.configure(highlightthickness=2, highlightbackground="#b4b4b6")

    def refresh_label_on_click(self, event):
        self.refresh_label.configure(highlightthickness=3, highlightbackground="#9d9d9e")
        self.refresh_label_off_hover(event)
        self.clear_entries()
        self.load_tree()