from tkinter import *
from tkinter import PhotoImage
import webbrowser
import smtplib
from tkmacosx import Button as button
import database as db
from tkinter import messagebox
from tkinter import simpledialog

import course_module as cmod
import attendance as atd
import grades as gds
import forum_qa as qa

curr_frame = None
tabs = None


# Login screen
def widgets(window):
    frame0 = LabelFrame(window, bg="white", width=1280, height=720)
    frame0.pack()

    global curr_frame
    curr_frame = frame0

    photo = PhotoImage(file="images/loginpage2.png")
    label = Label(frame0, image=photo)
    label.image = photo
    label.place(x=0, y=0, relwidth=1, relheight=1)

    # Main login frame
    frame1 = Label(frame0, bg="#3d84b8", width=38, height=12)
    frame1.place(x=750, y=370, )
    # Login word above the entry
    frame2 = Label(frame0, bg="#3d84b8", foreground="white", text="LOGIN", font="Helvetica")
    frame2.place(x=784, y=400)

    # Username Entry
    def click_username(event):
        username.config(state=NORMAL)
        username.delete(0, END)

    username = Entry(frame0, width=10)
    username.insert(0, "Username")
    username.config(state=DISABLED)
    username.bind("<Button-1>", click_username)
    username.pack()
    username.place(x=788, y=440, height=38, width=192)
    # Password Entry
    def click_password(event):
        password.config(state=NORMAL)
        password.delete(0, END)

    password = Entry(frame0, width=16, show="*")
    password.insert(0, "Password")
    password.config(state=DISABLED)
    password.bind("<Button-1>", click_password)
    password.pack()
    password.place(x=788, y=480, height=38, width=192)

    # Login button
    btn = button(frame0, bg="#00adb5", text="Log in", font="Helvetica", fg="white",
                 command=lambda: log_click(window, password, username))
    btn.place(x=983, y=440, height=78, width=85, )

    # Forget ID or Password button
    forgot_ip = button(frame0, text="Forget ID or Password?",
                       command=lambda: forgot_password_click(), fg="white", bg='#3d84b8', highlightthickness=0)
    forgot_ip.place(x=795, y=530)

    # Black Frame
    frame4 = Label(frame0, bg="#393e46", width=17, height=12)
    frame4.place(x=1110, y=372)

    # Creating Labels for hyperlinks and make it functions when clicked.
    def callback(url):
        webbrowser.open_new(url)
    # Label for Manual hyperlink
    frame5 = Label(frame0, text="Manual  >", fg="white", bg="#00adb5", width=10, height=2)
    frame5.place(x=750, y=600)
    frame5.bind("<Button-1>", lambda e: callback("https://learn.inha.ac.kr/local/ubion/manual/"))
    # Label for Q&A hyperlink
    frame6 = Label(frame0, text="Q&A  >", fg="white", bg="#00adb5", width=10, height=2)
    frame6.place(x=876, y=600)
    frame6.bind("<Button-1>", lambda e: callback("https://learn.inha.ac.kr/local/ubion/manual/"))
    # Label for FAQ hyperlink
    frame7 = Label(frame0, text="FAQ  >", fg="white", bg="#00adb5", width=10, height=2)
    frame7.place(x=1002, y=600)
    frame7.bind("<Button-1>", lambda e: callback("https://learn.inha.ac.kr/local/ubion/manual/"))

    # Links label in the black frame
    def callback(url):
        webbrowser.open_new(url)
    # Inha University
    link1 = Label(frame0, text="INHA UNIVERSITY", bg="#393e46", fg="white", cursor="hand2", )
    link1.place(x=1131, y=400)
    link1.bind("<Button-1>", lambda e: callback("https://www.inha.ac.kr/kr/index.do"))
    # Inha Portal
    link2 = Label(frame0, text="INHA Portal", bg="#393e46", fg="white", cursor="hand2")
    link2.place(x=1131, y=430)
    link2.bind("<Button-1>", lambda e: callback("https://portal.inha.ac.kr/"))
    # Jungseok Library
    link3 = Label(frame0, text="Jungseok Library", bg="#393e46", fg="white", cursor="hand2")
    link3.place(x=1131, y=460)
    link3.bind("<Button-1>", lambda e: callback("https://lib.inha.ac.kr/kor/"))
    # Sugang
    link4 = Label(frame0, text="Course Registerati..", bg="#393e46", fg="white", cursor="hand2")
    link4.place(x=1131, y=490)
    link4.bind("<Button-1>", lambda e: callback("https://sugang.inha.ac.kr/sugang/"))
    # Inha Plaza
    link5 = Label(frame0, text="INHA Plaza", bg="#393e46", fg="white", cursor="hand2")
    link5.place(x=1131, y=520)
    link5.bind("<Button-1>", lambda e: callback("https://plaza.inha.ac.kr/plaza/index.do"))
#
# Log in when clicked
def log_click(window, password, username):

    username_db = db.students.get("12210420")[3]
    password_db = db.students.get("12210420")[4]

    if username.get() == username_db and password.get() == password_db:
        curr_frame.destroy()

        # tabs frame is loaded
        global tabs
        tabs = display_tabs(window)

    else:
        messagebox.showinfo("Please try again", f"{username.get()} or {password.get()} is not correct  please  try again!")
#
# smtplib to send emafegil to any email account
def forgot_password_click():
    # simpledialog to get email from user
    myvar = simpledialog.askstring("We will send your password via email", "Please enter your email address")
    send_email(myvar)

# User's email account
def send_email(email):
    sender = "your email address"
    receivers = [email]

    # message appears in your email after email is sent
    message = 'Subject: {}\n\n{}'.format("INHA I-CLASS", "Your Password is 'mypassword' ")

    gmail_user = 'your email address' # You can check your email
    gmail_app_password = "your google app password" # First you need to insert google app password otherwise it doesn't work
    sent_from = 'email address which will be sent from'
    sent_to = email
    email_text = message

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_app_password)
        server.sendmail(sent_from, sent_to, email_text)
        server.close()
        # it appears on your Pycharm console
        print('Email sent!')
    except Exception as exception:
        print("Error: %s!\n\n" % exception)
#


def display_tabs(window):
    # Create a frame where every tabs are gathered
    main_frame = LabelFrame(window, bg="white", width=1280, height=40)
    main_frame.pack()

    b1 = Button(main_frame, text="Course Modules", command=lambda: display_mod(window), padx=20, pady=5)
    b1.place(x=1, y=1)

    b2 = Button(main_frame, text="Course Attendance", command=lambda: display_att(window), padx=20, pady=5)
    b2.place(x=135, y=1)

    b3 = Button(main_frame, text="Course Grades", command=lambda: display_grades(window), padx=20, pady=5)
    b3.place(x=284, y=1)

    b4 = Button(main_frame, text="Q&A Forum", command=lambda: display_forum(window), padx=20, pady=5)
    b4.place(x=408, y=1)

    b5 = Button(main_frame, text="Log out", command=lambda: log_out(window), padx=20, pady=5)
    b5.place(x=1185, y=1)

    # When display_tabs is called, the global variable "tabs" becomes the main_frame created in this function.
    # In this way, when the user log out (see func. "log_out"), the tabs frame is unloaded.
    return main_frame


def display_mod(window):
    global curr_frame
    # Avoid to stack several frame
    if curr_frame is not None:
        curr_frame.destroy()
    # Update the global variable + load Modules screen
    curr_frame = cmod.widgets(window)


def display_att(window):
    global curr_frame
    # Avoid to stack several frame
    if curr_frame is not None:
        curr_frame.destroy()
    # Update the global variable + load Attendance screen
    curr_frame = atd.widgets(window)


def display_grades(window):
    global curr_frame
    # Avoid to stack several frame
    if curr_frame is not None:
        curr_frame.destroy()
    # Update the global variable + load Grades screen
    curr_frame = gds.widgets(window)


def display_forum(window):
    global curr_frame
    # Avoid to stack several frame
    if curr_frame is not None:
        curr_frame.destroy()
    # Update the global variable + load Q&A screen
    curr_frame = qa.widgets(window)


def log_out(window):
    global curr_frame
    # Avoid to stack several frame
    if curr_frame is not None:
        curr_frame.destroy()
    if tabs is not None:
        tabs.destroy()
    # Load the login screen
    widgets(window)
