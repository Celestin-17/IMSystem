import sys
import smtplib
import random
from userFrame import *
from userFrame import UserFrame
import tkinter as tk
from tkinter import PhotoImage
from tkinter.simpledialog import askstring
import credentials
import dbHandler
import adminFrame


class MainFrame():
    """ Initializes Login User Interface"""
    def __init__(self, parent):
        self.parent = parent
        self.db_params = credentials.connection_params
        self.smtp_email = credentials.SMTP_EMAIL
        self.smtp_pwd = credentials.SMTP_PASSWORD
        self.timezone = pytz.timezone("Europe/Bucharest")
        self.title_img = PhotoImage(file="./images/stock_heading.png")
        self.passlabel_img = PhotoImage(file="./images/passlabel_img.png")
        self.userlabel_img = PhotoImage(file="./images/userlabel_img.png")
        self.or_label_img = PhotoImage(file="./images/or_label_img.png")
        self.user_img = PhotoImage(file="./images/user.png")
        self.regimg = PhotoImage(file="./images/regimg.png")
        self.login_button_img = PhotoImage(file="./images/arrow.png")
        self.signup_img = PhotoImage(file="./images/signup_img.png")
        self.cpass_img = PhotoImage(file="./images/confirm.png")
        self.mail_img = PhotoImage(file="./images/email.png")
        self.back_img = PhotoImage(file="./images/back.png")
        self.header1_img = PhotoImage(file="./images/header1.png")
        self.header2_img = PhotoImage(file="./images/header2.png")
        self.hide_img = PhotoImage(file="./images/hide.png")
        self.show_img = PhotoImage(file="./images/show.png")
        self.exit_img = PhotoImage(file="./images/switch.png")
        self.bgcolor = "#ecebeb"
        self.emp_id = None
        self.hidden_pwd = True
        self.GUI()
    def __del__(self):
        sys.exit(0)


    def GUI(self):
        self.frame = tk.Frame(self.parent, height=900, width=860, bg=self.bgcolor)
        self.frame.pack()
        self.today_header = tk.Label(self.parent, text="", bg=self.bgcolor,
                                     foreground="black", font=("Arial", 14, "italic"))
        self.today_header.place(x=420, y=875)
        self.timenow_header = tk.Label(self.parent, text="", bg=self.bgcolor, foreground="black",
                                       font=("Arial", 14, "italic"))
        self.timenow_header.place(x=337, y=875)
        self.login_button = tk.Label(self.parent, image=self.login_button_img,
                                     bg=self.bgcolor, activebackground=self.bgcolor)
        self.login_button.place(x=385, y=610)
        self.login_button.bind("<Enter>", self.on_event)
        self.login_button.bind("<Button>", self.on_click)
        self.login_button.bind("<Leave>", self.on_default)
        self.forgotten_pass = tk.Label(self.parent, text="Forgotten password?", fg="blue", bg=self.bgcolor,
                                       font=("Arial", 12, "normal"), cursor="hand2")
        self.forgotten_pass.place(x=288, y=570)
        self.forgotten_pass.bind("<Button-1>", self.recover_on_click)
        self.user_img = self.user_img.subsample(2, 2)
        self.userimg_label = tk.Label(self.parent, image=self.user_img, bg=self.bgcolor)
        self.userimg_label.place(x=370, y=265)
        self.passlabel = tk.Label(self.parent, image=self.passlabel_img, bg=self.bgcolor)
        self.passlabel.place(x=355, y=500)
        self.userlabel = tk.Label(self.parent, image=self.userlabel_img, bg=self.bgcolor)
        self.userlabel.place(x=350, y=419)
        self.header1_label = tk.Label(self.parent, image=self.header1_img, bg=self.bgcolor)
        self.header1_label.place(x=290, y=60)
        self.header2_img = self.header2_img.subsample(2, 2)
        self.header2_label = (tk.Label(self.parent, image=self.header2_img, bg=self.bgcolor))
        self.header2_label.place(x=180, y=130)
        self.hide_label = tk.Label(self.parent, image=self.hide_img, bg=self.bgcolor)
        self.hide_label.place(x=570, y=541)
        self.hide_label.bind("<Button>", self.hide_on_click)
        self.exit_label = tk.Label(self.parent, image=self.exit_img, bg=self.bgcolor)
        self.exit_label.place(x=740, y=20)
        self.exit_label.bind("<Enter>", self.exit_on_hover)
        self.exit_label.bind("<Button>", self.exit_on_click)
        self.exit_label.bind("<Leave>", self.exit_off_hover)

        self.empid_entry = tk.Entry(self.parent, width=30, font=("Arial", 16, "bold"),
                                    bg="white", fg="black", highlightbackground="white", highlightthickness=0)
        self.empid_entry.place(x=290, y=462)
        self.empid_entry.focus()
        self.password_entry = tk.Entry(self.parent, width=30, font=("Arial", 16, "normal"),
                                    bg="white", fg="black", show="*", highlightthickness=0, highlightbackground="white")
        self.password_entry.place(x=290, y=545)
        self.update_clock()

    def exit_on_click(self, event):
        self.exit_label.configure(highlightthickness=3, highlightbackground="#9d9d9e")
        self.exit_off_hover(event)
        self.option = tk.messagebox.askquestion("Inventory Manager", "You are going to terminate the program !"
                                                                     "\nAre you sure?")
        if self.option == "yes": self.__del__()
        else: return

    def exit_off_hover(self, event):
        event.widget.configure(activebackground=self.bgcolor, highlightthickness=0, highlightbackground=self.bgcolor)

    def exit_on_hover(self, event):
        self.exit_label.configure(highlightthickness=2, highlightbackground="#b4b4b6")

    def generate_newpass(self):  # For password recovery
        self.new_pass = "".join([random.choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)") for i in range(15)])
        return self.new_pass

    def clear_entries(self):
        self.empid_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

    def on_event(self, event):
        self.login_button.configure(activebackground="#FFFFFF", highlightthickness=2, highlightbackground="#b4b4b6")

    def on_default(self, event):
        event.widget.configure(activebackground=self.bgcolor, highlightthickness=0, highlightbackground="#b4b4b6")

    def on_click(self, event):   ## Login command
        self.login_button.configure(highlightthickness=3, highlightbackground="#9d9d9e")
        self.on_default(event)
        self.emp_id = self.empid_entry.get()
        self.pass_entry = self.password_entry.get()
        if self.empid_entry == "" or self.pass_entry == "":
            self.clear_entries()
            return tk.messagebox.showerror("System", "You can't leave empty spaces !")
        else:
            self.credentials = [self.emp_id, self.pass_entry]
            self.response = dbHandler.DBHandler.login(self, self.credentials)
            if self.response is False:
                self.clear_entries()
                return tk.messagebox.showerror("Inventory Manager", "Your ID/Password is incorrect !")
            else:
                self.name = self.response[0][0]
                self.usertype = self.response[0][1]
                self.clear_entries()
                self.frame.destroy()
                self.isAdmin = dbHandler.DBHandler.user_state(self, self.emp_id)
                if self.isAdmin:
                    self.app = adminFrame.AdminFrame(self.parent, self.name, self.isAdmin, self.emp_id)
                else:
                    self.app = UserFrame(self.parent, self.name, self.isAdmin, self.emp_id)
    def hide_on_click(self, event):
        if self.hidden_pwd:
            self.password_entry.configure(show="", )
            self.hide_label.destroy()
            self.show_label = tk.Label(self.parent, image=self.show_img, bg=self.bgcolor)
            self.show_label.place(x=570, y=541)
            self.show_label.bind("<Button>", self.hide_on_click)
            self.hidden_pwd = False
        else:
            self.password_entry.configure(show="*")
            self.show_label.destroy()
            self.hide_label = tk.Label(self.parent, image=self.hide_img, bg=self.bgcolor)
            self.hide_label.place(x=570, y=541)
            self.hide_label.bind("<Button>", self.hide_on_click)
            self.hidden_pwd = True

    def recover_on_click(self, evemt):
        self.email = askstring("Password Recovery", "To proceed with the password recovery, "
                                                    "please enter your email:\n\n")
        if self.email is None: return tk.messagebox.showinfo("Inventory Manager", "Operation aborted")
        self.first_check = False
        self.second_check = False
        for char in self.email:  # checks '@' and '.' existence
            if char == "@":
                self.first_check = True
            elif char == ".":
                self.second_check = True
        if not self.first_check or not self.second_check:
            return tk.messagebox.showerror("Inventory Manager", "You must complete a valid email !")
        self.response = dbHandler.DBHandler.check_email(self, self.email)
        if not self.response:
            return tk.messagebox.showerror("Inventory Manager", "There is no account associated with this email !")
        self.date = str(self.response[0][0]).split()[0]
        self.emp_id = self.response[0][1]
        self.user_bday = askstring("Password Recovery", "Ok, now please enter your date of birth " 
                                                        "(YYYY-MM-DD): \n\n")
        if self.user_bday == self.date:
            self.new_pass = self.generate_newpass()
            self.container = [self.new_pass, self.emp_id]
            self.response = dbHandler.DBHandler.update_password(self, self.container)
            if self.response:
                self.params = [self.new_pass, self.email]
                self.send_recoverypass(self.params)
                return tk.messagebox.showinfo("Password Recovery", "Your new password has been sent to the email address ! ")
            else: return
        else: return tk.messagebox.showerror("Password Recovery", "Your date of birth is incorrect !")

    def send_recoverypass(self, params):
        self.newkey = params[0]
        self.email = params[1]
        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(self.smtp_email, self.smtp_pwd)
                message = f"Subject:IMS Reset Password !\n\nThere is your new generated password: {self.newkey}"
                server.sendmail(self.smtp_email, self.email, msg=message)
        except Exception as e:
            print(f"SMTP: Error encountered ({e})")
    def update_clock(self):
        self.raw_ts = dt.datetime.now(self.timezone)
        self.date_now = self.raw_ts.strftime("%d %b %Y")
        self.time_now = self.raw_ts.strftime("%H:%M:%S %p")
        self.timenow_header.config(text=self.date_now)
        self.today_header.config(text=f" | {self.time_now}")
        self.today_header.after(1000, self.update_clock)

    def clear_entries(self):
        self.empid_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)