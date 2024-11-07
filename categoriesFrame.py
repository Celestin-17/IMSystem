import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
import credentials
import datetime as dt
import pytz
import adminFrame
import dbHandler
import mainFrame


class CategoriesFrame():
    """ Initializes Product Categories Frame (only for Admins) """
    def __init__(self, parent, user, isAdmin:bool, emp_id:int):
        self.parent = parent
        self.user = user
        self.isAdmin = isAdmin
        self.emp_id = emp_id
        self.db_params = credentials.connection_params
        self.totalcats_intvar = tk.IntVar()
        self.updating = False
        self.timezone = pytz.timezone("Europe/Bucharest")
        self.title_img = PhotoImage(file="./images/stock_heading.png")
        self.passlabel_img = PhotoImage(file="./images/passlabel_img.png")
        self.userlabel_img = PhotoImage(file="./images/userlabel_img.png")
        self.or_label_img = PhotoImage(file="./images/or_label_img.png")
        self.refresh_img = PhotoImage(file="./images/refresh.png")
        self.title2_img = PhotoImage(file="./images/user.png")
        self.regimg = PhotoImage(file="./images/regimg.png")
        self.logout_img = PhotoImage(file="./images/logout.png")
        self.login_button_img = PhotoImage(file="./images/arrow.png")
        self.signup_img = PhotoImage(file="./images/signup_img.png")
        self.cpass_img = PhotoImage(file="./images/confirm.png")
        self.mail_img = PhotoImage(file="./images/email.png")
        self.back_img = PhotoImage(file="./images/back.png")
        self.cat_header = PhotoImage(file="./images/categories_header.png")
        self.add_newcat_img = PhotoImage(file="./images/add_newcat.png")
        self.catname_img = PhotoImage(file="./images/catname.png")
        self.totalcats_img = PhotoImage(file="./images/total_cats.png")
        self.logout_label_img = PhotoImage(file="./images/logout_label.png")
        self.add_img = PhotoImage(file="./images/add.png")
        self.remove_img = PhotoImage(file="./images/remove.png")
        self.reset_img = PhotoImage(file="./images/undo.png")
        self.bgcolor = "#ecebeb"
        self.GUI()

    def GUI(self):
        self.frame = tk.Frame(self.parent, height=900, width=860, bg=self.bgcolor)
        self.frame.pack()

        self.welcome_label = tk.Label(self.parent, text="", background=self.bgcolor,
                                      foreground="black", font=("Arial", 35, "normal"))
        self.welcome_label.place(x=350, y=150)
        self.header = tk.Label(self.parent, image=self.cat_header, bg=self.bgcolor)
        self.header.place(x=175, y=25)
        self.newcat_label = tk.Label(self.parent, image=self.add_newcat_img, bg=self.bgcolor)
        self.newcat_label.place(x=60, y=135)
        self.catname_label = tk.Label(self.parent, image=self.catname_img, bg=self.bgcolor)
        self.catname_label.place(x=98, y=255)
        self.add_img = self.add_img.subsample(2, 2)
        self.addcat_label = tk.Label(self.parent, image=self.add_img, bg=self.bgcolor)
        self.addcat_label.place(x=80, y=400)
        self.addcat_label.bind("<Button>", self.addcat_on_click)
        self.addcat_label.bind("<Enter>", self.addcat_on_hover)
        self.addcat_label.bind("<Leave>", self.addcat_off_hover)
        self.remove_img = self.remove_img.subsample(2, 2)
        self.removecat_label = tk.Label(self.parent, image=self.remove_img, bg=self.bgcolor)
        self.removecat_label.place(x=300, y=400)
        self.removecat_label.bind("<Enter>", self.remove_on_hover)
        self.removecat_label.bind("<Button>", self.remove_on_click)
        self.removecat_label.bind("<Leave>", self.remove_off_hover)
        self.resetcat_label = tk.Label(self.parent, image=self.reset_img, bg=self.bgcolor)
        self.resetcat_label.place(x=190, y=400)
        self.resetcat_label.bind("<Enter>", self.reset_on_hover)
        self.resetcat_label.bind("<Button>", self.reset_on_click)
        self.resetcat_label.bind("<Leave>", self.reset_off_hover)

        self.catname_entry = tk.Entry(self.parent, width=24, bg="white", highlightthickness=0,
                                      highlightbackground=self.bgcolor,fg="black", font=("Arial", 15, "normal"))
        self.catname_entry.place(x=110, y=330)

        # self.addcat_button = tk.Button(self.parent, text="Add", width=10, bg=self.bgcolor,
        #                                highlightbackground=self.bgcolor, highlightthickness=0)
        # self.addcat_button.place(x=90, y=375)
        # self.removecat_button = tk.Button(self.parent, text="Remove", width=10, bg=self.bgcolor,
        #                                highlightbackground=self.bgcolor, highlightthickness=0)
        # self.removecat_button.place(x=215, y=375)\

        self.logout_img = self.logout_img.subsample(2, 2)
        # self.logout = tk.Label(self.parent, image=self.logout_img, bg=self.bgcolor)
        # self.logout.place(x=650, y=750)

        self.logout = tk.Label(self.parent, image=self.logout_img, background=self.bgcolor)
        self.logout.place(x=760, y=55)
        self.logout.bind("<Enter>", self.logout_on_hover)
        self.logout.bind("<Button>", self.logout_on_click)
        self.logout.bind("<Leave>", self.logout_off_hover)
        self.logout_label_img = self.logout_label_img.subsample(2, 2)
        self.logout_label = ttk.Label(self.parent, image=self.logout_label_img, background=self.bgcolor)
        self.logout_label.place(x=740, y=10)

        self.today_header = tk.Label(self.parent, text="", bg=self.bgcolor,
                                     foreground="black", font=("Arial", 14, "italic"))
        self.today_header.place(x=420, y=870)
        self.timenow_header = tk.Label(self.parent, text="", bg=self.bgcolor, foreground="black",
                                       font=("Arial", 14, "italic"))
        self.timenow_header.place(x=337, y=870)

        self.back_img = self.back_img.subsample(2, 2)
        self.go_back = tk.Label(self.parent, image=self.back_img, bg=self.bgcolor)
        self.go_back.place(x=30, y=35)
        self.go_back.bind("<Enter>", self.back_on_hover)
        self.go_back.bind("<Button>", self.back_on_click)
        self.go_back.bind("<Leave>", self.back_off_hover)
        self.totalcats_label = tk.Label(self.parent, image=self.totalcats_img, bg=self.bgcolor)
        self.totalcats_label.place(x=430, y=580)
        self.totalcats_nr = tk.Label(self.parent, textvariable=self.totalcats_intvar, fg="#0d92fc", bg=self.bgcolor, font=("Arial", 38, "bold"))
        self.totalcats_nr.place(x=725, y=585)

        self.refresh_img = self.refresh_img.subsample(2, 2)
        self.refresh_label = tk.Label(self.parent, image=self.refresh_img, background=self.bgcolor)
        self.refresh_label.place(x=785, y=325)
        self.refresh_label.bind("<Enter>", self.refresh_on_hover)
        self.refresh_label.bind("<Button>", self.refresh_on_click)
        self.refresh_label.bind("<Leave>", self.refresh_off_hover)

        self.style = ttk.Style(self.parent)
        self.style.theme_use("clam")

        self.tree = ttk.Treeview(height=20, columns=2)
        self.style.configure("Treeview", background="white", foreground="black", fieldbackground="white")
        self.tree["columns"] = ("CatID", "Category")
        self.tree.column("#0", width=0, minwidth=0)
        self.tree.column("CatID", width=150, minwidth=65)
        self.tree.column("Category", width=150, minwidth=65)
        self.tree.heading("#0", text="Label", anchor="w")
        self.tree.heading("CatID", text="CatID")
        self.tree.heading("Category", text="Category")

        self.tree.place(x=450, y=150)
        self.tree.bind("<ButtonRelease>", self.tree_on_click)
        self.load_categories()
        self.update_clock()

    def tree_on_click(self, event):
        self.updating = True
        self.iid = self.tree.focus()
        self.tree.selection_set(self.iid)
        self.item = self.tree.item(self.iid)
        self.category = self.item["values"][1]
        if self.category == None: return
        else:
            self.clear_entries()
            print(f"category: {self.category}")
            self.catname_entry.insert(0, self.category)

    def clear_focus(self):
        for i in self.tree.selection():
            self.tree.selection_remove(i)

    def clear_entries(self):
        self.catname_entry.delete(0, tk.END)

    def back_off_hover(self, event):
        event.widget.configure(activebackground=self.bgcolor, highlightthickness=0, highlightbackground=self.bgcolor)

    def back_on_hover(self, event):
        self.go_back.configure(highlightthickness=2, highlightbackground="#b4b4b6")

    def back_on_click(self, event):
        self.go_back.configure(highlightthickness=3, highlightbackground="#9d9d9e")
        self.back_off_hover(event)
        self.frame.destroy()
        self.app = adminFrame.AdminFrame(self.parent, self.user, self.isAdmin, self.emp_id)

    def reset_on_hover(self, event):
        self.resetcat_label.configure(highlightthickness=2, highlightbackground="#b4b4b6")

    def reset_on_click(self, event):
        self.resetcat_label.configure(highlightthickness=3, highlightbackground="#9d9d9e")
        self.reset_off_hover(event)
        self.updating = False
        self.clear_focus()
        self.clear_entries()

    def reset_off_hover(self, event):
        event.widget.configure(activebackground=self.bgcolor, highlightthickness=0, highlightbackground=self.bgcolor)

    def addcat_off_hover(self, event):
        event.widget.configure(activebackground=self.bgcolor, highlightthickness=0, highlightbackground=self.bgcolor)
    def addcat_on_click(self, event):
        self.addcat_label.configure(highlightthickness=3, highlightbackground="#9d9d9e")
        self.addcat_off_hover(event)
        self.new_cat = self.catname_entry.get()
        if self.new_cat == "": return tk.messagebox.showerror("Stock Manager", "You have to fill the entry !")
        if self.updating:
            self.iid = self.tree.focus()
            self.item = self.tree.item(self.iid)
            self.index = self.item["values"][0]
            self.catname = self.item["values"][1]
            self.option = tk.messagebox.askquestion("Stock Manager", f"You are going to rename category {self.catname} to "
                                                                     f"{self.new_cat} !\n\nAre you sure?")
            if self.option == "yes":
                self.container = [self.new_cat, self.index]
                self.response = dbHandler.DBHandler.update_category(self, self.container)
                if self.response:
                    self.updating = False
                    self.load_categories()
                    self.clear_entries()
                    self.clear_focus()
                    return tk.messagebox.showinfo("Stock Manager", f"You have succesfully renamed CatID:{self.index} !")
            else: return
        else:
            self.option = tk.messagebox.askquestion("Stock Manager", f"You are going to add a new category !\n\n"
                                                                     f"Category Name: {self.new_cat}\n\n"
                                                                     f"Are you sure?")
            if self.option == "yes":
                self.response = dbHandler.DBHandler.add_category(self, self.new_cat)
                if self.response:
                    self.updating = False
                    self.load_categories()
                    self.clear_focus()
                    self.clear_entries()
                    return tk.messagebox.showinfo("Stock Manager", f"You have succesfully added category: {self.new_cat}")
            else: return


    def addcat_on_hover(self, event):
        self.addcat_label.configure(highlightthickness=2, highlightbackground="#b4b4b6")

    def load_categories(self):
        self.cats = dbHandler.DBHandler.get_categories(self)
        for child in self.tree.get_children():
            self.tree.delete(child)
        self.count = 0
        for i in self.cats:
            self.count += 1
            self.tree.insert("", tk.END, values=(i[0], i[1]))
        self.totalcats = self.count
        self.totalcats_intvar.set(self.count)

    def update_clock(self):
        self.raw_ts = dt.datetime.now(self.timezone)
        self.date_now = self.raw_ts.strftime("%d %b %Y")
        self.time_now = self.raw_ts.strftime("%H:%M:%S %p")
        self.timenow_header.config(text=self.date_now)
        self.today_header.config(text=f" | {self.time_now}")
        self.today_header.after(1000, self.update_clock)

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

    def remove_off_hover(self, event):
        event.widget.configure(activebackground=self.bgcolor, highlightthickness=0, highlightbackground=self.bgcolor)

    def remove_on_hover(self, event):
        self.removecat_label.configure(highlightthickness=2, highlightbackground="#b4b4b6")

    def remove_on_click(self, event):
        self.removecat_label.configure(highlightthickness=3, highlightbackground="#9d9d9e")
        self.remove_off_hover(event)
        if not self.updating: return tk.messagebox.showerror("Stock Manager", "You must select an item first !")
        self.iid = self.tree.focus()
        self.item = self.tree.item(self.iid)
        self.index = self.item["values"][0]
        self.catname = self.item["values"][1]
        self.option = tk.messagebox.askquestion("Stock Manager", f"You are going to remove category: {self.catname} !"
                                                                 "\n\nAre you sure?")
        if self.option == "yes":
            self.response = dbHandler.DBHandler.remove_category(self, self.index)
            if self.response:
                self.updating = False
                self.load_categories()
                self.clear_focus()
                self.clear_entries()
                return tk.messagebox.showinfo("Stock Manager", f"You have succesfully removed category: {self.catname} !")
        else: return
    def refresh_off_hover(self, event):
        event.widget.configure(activebackground=self.bgcolor, highlightthickness=0, highlightbackground=self.bgcolor)

    def refresh_on_click(self, event):
        self.refresh_label.configure(highlightthickness=3, highlightbackground="#9d9d9e")
        self.refresh_off_hover(event)

    def refresh_on_hover(self, event):
        self.refresh_label.configure(highlightthickness=2, highlightbackground="#b4b4b6")
