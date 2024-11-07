import tkinter as tk
from tkinter import PhotoImage
from tkinter.simpledialog import askstring
import importlib
import credentials
import dbHandler
import random
import datetime as dt
import smtplib
import pytz


class SettingsFrame():
    """ Initializes User Account Settings Frame """
    def __init__(self, parent, user, isAdmin:bool, emp_id:int):
        self.parent = parent
        self.user = user
        self.isAdmin = isAdmin
        self.emp_id = emp_id
        self.db_params = credentials.connection_params
        self.smtp_email = credentials.SMTP_EMAIL
        self.smtp_pwd = credentials.SMTP_PASSWORD
        self.usertype_strvar = tk.StringVar()
        self.timezone = pytz.timezone("Europe/Bucharest")
        self.bgcolor = "#ecebeb"
        self.header_img = PhotoImage(file="images/settings_header.png")
        self.settings_img = PhotoImage(file="./images/settings.png")
        self.back_img = PhotoImage(file="./images/back.png")
        self.logout_img = PhotoImage(file="./images/logout.png")
        self.logout_label_img = PhotoImage(file="./images/logout_label.png")
        self.GUI()
        self.update_clock()


    def GUI(self):
        self.frame = tk.Frame(self.parent, height=900, width=900, bg=self.bgcolor)
        self.frame.pack()
        self.main_header = tk.Label(self.parent, image=self.header_img, bg=self.bgcolor)
        self.main_header.place(x=150, y=30)
        self.settings_img = self.settings_img.subsample(2, 2)
        self.header = tk.Label(self.parent, image=self.settings_img, bg=self.bgcolor)
        self.header.place(x=360, y=170)
        self.back_img = self.back_img.subsample(2, 2)
        self.go_back = tk.Label(self.parent, image=self.back_img, bg=self.bgcolor)
        self.go_back.place(x=30, y=20)
        self.go_back.bind("<Enter>", self.back_on_hover)
        self.go_back.bind("<Button>", self.back_on_click)
        self.go_back.bind("<Leave>", self.back_off_hover)
        self.logout_img = self.logout_img.subsample(2, 2)
        self.logout = tk.Label(self.parent, image=self.logout_img, background=self.bgcolor)
        self.logout.place(x=810, y=55)
        self.logout_label_img = self.logout_label_img.subsample(2, 2)
        self.logout_label = tk.Label(self.parent, image=self.logout_label_img, background=self.bgcolor)
        self.logout_label.place(x=783, y=10)
        self.logout.bind("<Enter>", self.logout_on_hover)
        self.logout.bind("<Button>", self.logout_on_click)
        self.logout.bind("<Leave>", self.logout_off_hover)
        self.username_label = tk.Label(self.parent, text="Username:", fg="black", bg=self.bgcolor,
                                       font=("Arial", 22, "normal"))
        self.username_label.place(x=200, y=400)
        self.userlabel_label = tk.Label(self.parent, text=f"{self.user}", bg=self.bgcolor, fg="black",
                                  font=("Arial", 22, "bold"))
        self.userlabel_label.place(x=330, y=400)
        self.usertype_label = tk.Label(self.parent, text="User type:", bg=self.bgcolor, fg="black",
                                       font=("Arial", 22, "normal"))
        self.usertype_label.place(x=200, y=440)
        self.usertype_label = tk.Label(self.parent, textvariable=self.usertype_strvar, bg=self.bgcolor, fg="black",
                                    font=("Arial", 22, "bold"))
        self.usertype_label.place(x=330, y=440)

        if self.isAdmin: self.usertype_strvar.set("ADMIN")
        else: self.usertype_strvar.set("Employee")

        self.empid_label = tk.Label(self.parent, text="Employee ID:", bg=self.bgcolor, fg="black",
                                    font=("Arial", 22, "normal"))
        self.empid_label.place(x=200, y=480)
        self.empid_intlabel = tk.Label(self.parent, text=f"{self.emp_id}", bg=self.bgcolor, fg="black",
                                       font=("Arial", 22, "bold"))
        self.empid_intlabel.place(x=345, y=480)
        self.user_data = dbHandler.DBHandler.get_userdata(self, self.emp_id)
        self.user_pass = self.user_data[0][2]
        self.user_email = self.user_data[0][3]
        self.user_gender = self.user_data[0][4]
        self.user_birthday = self.user_data[0][5]
        self.user_phone = self.user_data[0][6]
        self.user_address = self.user_data[0][9]
        self.password_label = tk.Label(self.parent, text="Password:", bg=self.bgcolor, fg="black",
                                       font=("Arial", 22, "normal"))
        self.password_label.place(x=200, y=520)
        self.hidden_pass = tk.Label(self.parent, text=f"{"".join(["*" for _ in range(len(self.user_pass))])}", bg=self.bgcolor,
                                    fg="black", font=("Arial", 22, "bold"))
        self.hidden_pass.place(x=320, y=520)
        self.password_button = tk.Button(self.parent, text="Change password", width=15, height=2, bg=self.bgcolor,
                                         font=("Arial", 13, "bold"), highlightthickness=0, fg="black",
                                         highlightbackground=self.bgcolor, command=self.change_password)
        self.password_button.place(x=470, y=520)
        self.email_button = tk.Button(self.parent, text="Change email", width=15, height=2, bg=self.bgcolor, fg="black",
                                         font=("Arial", 13, "bold"), highlightthickness=0, command=self.change_email,
                                      highlightbackground=self.bgcolor)
        self.email_button.place(x=630, y=520)
        self.email_label = tk.Label(self.parent, text="Email:", bg=self.bgcolor, fg="black", font=("Arial", 22, "normal"))
        self.email_label.place(x=200, y=560)
        self.email_userlabel = tk.Label(self.parent, text=f"{self.user_email}", bg=self.bgcolor, fg="black", font=("Arial", 22, "bold"))
        self.email_userlabel.place(x=280, y=560)
        self.birthday_label = tk.Label(self.parent, text="Date of birth:", bg=self.bgcolor, fg="black", font=("Arial", 22, "normal"))
        self.birthday_label.place(x=200, y=600)
        self.user_dob = tk.Label(self.parent, text=f"{self.user_birthday}", bg=self.bgcolor, fg="black", font=("Arial", 22, "bold"))
        self.user_dob.place(x=335, y=600)
        self.phone_label = tk.Label(self.parent, text="Phone number:", bg=self.bgcolor, fg="black", font=("Arial", 22, "normal"))
        self.phone_label.place(x=200, y=640)
        self.user_phonelabel = tk.Label(self.parent, text=f"{self.user_phone}", bg=self.bgcolor, fg="black", font=("Arial", 22, "bold"))
        self.user_phonelabel.place(x=360, y=640)
        self.phone_button = tk.Button(self.parent, text="Change phone number", bg=self.bgcolor, fg="black", width=17,
                                      font=("Arial", 15, "bold"), highlightthickness=0, command=self.update_phone,
                                      height=2, highlightbackground=self.bgcolor)
        self.phone_button.place(x=540, y=632)
        self.user_addresslabel = tk.Label(self.parent, text="Address:", bg=self.bgcolor, fg="black", font=("Arial", 22, "normal"))
        self.user_addresslabel.place(x=200, y=680)
        self.address_label = tk.Label(self.parent, text=f"{self.user_address}", fg="black", bg=self.bgcolor,
                                         font=("Arial", 22, "bold"))
        self.address_label.place(x=300, y=680)
        self.today_header = tk.Label(self.parent, text="", bg=self.bgcolor,
                                     foreground="black", font=("Arial", 14, "italic"))
        self.today_header.place(x=420, y=870)
        self.timenow_header = tk.Label(self.parent, text="", bg=self.bgcolor, foreground="black",
                                       font=("Arial", 14, "italic"))
        self.timenow_header.place(x=337, y=870)
    def generate_newpass(self):
        self.new_pass = "".join([random.choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)") for _ in range(15)])
        return self.new_pass

    def back_on_click(self, event):
        self.go_back.configure(highlightthickness=3, highlightbackground="#9d9d9e")
        self.back_off_hover(event)
        if self.isAdmin:
            self.mod = importlib.import_module("adminFrame")
            self.frame.destroy()
            self.app = self.mod.AdminFrame(self.parent, self.user, self.isAdmin, self.emp_id)
        else:
            self.mod = importlib.import_module("userFrame")
            self.frame.destroy()
            self.app = self.mod.UserFrame(self.parent, self.user, self.isAdmin, self.emp_id)

    def change_password(self):
        self.response = dbHandler.DBHandler.get_userpass(self, self.emp_id)
        self.user_pass = self.response[0][0]
        self.old_pass = askstring("Reset Password", "Please enter your old password: \n", show="*")
        if self.old_pass is None: return tk.messagebox.showerror("Reset Password", "Operation aborted")
        if self.old_pass == self.user_pass:
            self.new_pass = askstring("Reset Password", "Please enter your new password: \n", show="*")
            self.confirmed_pass = askstring("Reset Password", "Please re-enter your new password: \n", show="*")
            if self.new_pass != self.confirmed_pass:
                return tk.messagebox.showerror("Reset Password", "The password you entered doesn't match, retry !")
            self.container = [self.new_pass, self.emp_id]
            self.response = dbHandler.DBHandler.update_password(self, self.container)
            if self.response:
                self.hidden_pass.config(text=f"{"".join(["*" for _ in range(len(self.new_pass))])}")
                return tk.messagebox.showinfo("Reset Password", "You have succesfully changed your password !")
        else: return tk.messagebox.showerror("Reset Password", "You entered an incorrect password !")


    def change_email(self):
        self.actual_pass = dbHandler.DBHandler.get_userpass(self, self.emp_id)
        self.real_pass = self.actual_pass[0][0]
        self.user_password = askstring("Inventory Manager", "Please enter your password first: \n")
        if self.user_password is None: return tk.messagebox.showerror("Inventory Manager", "Operation aborted")
        if str(self.real_pass) == str(self.user_password):
            self.new_mail = askstring("Inventory Manager", "Please enter your new email: \n")
            self.key_pass = self.generate_newpass()
            try:
                with smtplib.SMTP("smtp.gmail.com", 587) as server:
                    server.starttls()
                    server.login(self.smtp_email, self.smtp_pwd)
                    message = (f"Subject:IMS Reset Email Confirmation !\n\nThere is the confirmation key for approving the "
                               f"email change: {self.key_pass}")
                    server.sendmail(self.smtp_email, self.new_mail, msg=message)
            except Exception as e:
                print(f"SMTP: Error encountered ({e})")
            self.keypass_confirmation = askstring("Key Pass Confirmation", "A confirmation key has been sent to"
                                                                           "your new email address!\nPlease enter it in the field below: \n")
            if self.keypass_confirmation == self.key_pass:
                self.response = dbHandler.DBHandler.update_email(self, self.new_mail, self.emp_id)
                if self.response:
                    self.email_userlabel.config(text=f"{self.new_mail}")
                    return tk.messagebox.showerror("Key Pass Confirmation", "You have succesfully updated your email !")
                else: return tk.messagebox.showerror("Key Pass Confirmation", "Email updating failed !")
            else: return tk.messagebox.showerror("Key Pass Confirmation", "Incorrect validation key, retry !")
        else: return tk.messagebox.showerror("Key Pass Confirmation", "You entered an incorrect password !")

    def update_phone(self):
        self.new_phone = askstring("Inventory Manager", "Please enter your new phone number: \n")
        if self.new_phone is None: return tk.messagebox.showerror("Inventory Manage", "Operation aborted")
        self.response = dbHandler.DBHandler.update_phone(self, self.new_phone, self.emp_id)
        if self.response:
            self.user_phonelabel.config(text=f"{self.new_phone}")
            return tk.messagebox.showinfo("Inventory Manager", "You have succesfully updated your phone number !")

    def update_clock(self):
        self.raw_ts = dt.datetime.now(self.timezone)
        self.date_now = self.raw_ts.strftime("%d %b %Y")
        self.time_now = self.raw_ts.strftime("%H:%M:%S %p")
        self.timenow_header.config(text=self.date_now)
        self.today_header.config(text=f" | {self.time_now}")
        self.today_header.after(1000, self.update_clock)

    def back_off_hover(self, event):
        event.widget.configure(activebackground=self.bgcolor, highlightthickness=0, highlightbackground=self.bgcolor)

    def back_on_hover(self, event):
        self.go_back.configure(highlightthickness=2, highlightbackground="#b4b4b6")

    def logout_off_hover(self, event):
        event.widget.configure(activebackground=self.bgcolor, highlightthickness=0, highlightbackground=self.bgcolor)

    def logout_on_hover(self, event):
        self.logout.configure(highlightthickness=2, highlightbackground="#b4b4b6")

    def logout_on_click(self, event):
        self.logout.configure(highlightthickness=3, highlightbackground="#9d9d9e")
        self.logout_off_hover(event)
        self.mbox = tk.messagebox.askquestion("System", "You are going to be logged out !\n Are you sure?")
        if self.mbox == "yes":
            self.mod = importlib.import_module("mainFrame")
            self.frame.destroy()
            self.app = self.mod.MainFrame(self.parent)
        else: return
