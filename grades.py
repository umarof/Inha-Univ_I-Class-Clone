
################################################################
from tkinter import *
from tkinter import ttk

curr_frame = None
current_course = None

#region DO NOT TOUCH
def widgets(window):
    # Creating new frame and updating the current frame
    global curr_frame
    frame = Frame(window, bg="#005799", width=1280, height=680)
    frame.place(x=0, y=40)
    curr_frame = frame

    title = Label(frame, bg='#005799', fg='white', text="Course Grades", font=("Roboto", 40))
    title.place(x=410, y=20)

    courses = ['maths1', 'sw', 'maths2', 'computer', 'eng']
    images_and_names = []
    for c in courses:
        img = PhotoImage(file='images/img_' + c + '.png', master=frame)
        images_and_names.append((img, c))

    buttons = []
    for i in images_and_names:
        t = i[1]
        if t == 'sw':
            btn = Button(frame, image=i[0], command=lambda: [sw_current(), load_course(i[1], window)], height=92,
                         width=911)
        elif t == 'maths1':
            btn = Button(frame, image=i[0], command=lambda: [maths1_current(), load_course(i[1], window)], height=92,
                         width=911)
        elif t == 'maths2':
            btn = Button(frame, image=i[0], command=lambda: [maths2_current(), load_course(i[1], window)], height=92,
                         width=911)
        elif t == 'computer':
            btn = Button(frame, image=i[0], command=lambda: [computer_current(), load_course(i[1], window)], height=92,
                         width=911)
        elif t == 'eng':
            btn = Button(frame, image=i[0], command=lambda: [eng_current(), load_course(i[1], window)], height=92,
                         width=911)
        else:
            btn = Button(frame, image=i[0], command=lambda: load_course('Course', window), height=92, width=911)
        buttons.append(btn)

    y = 110
    for b in buttons:
        b.place(x=184, y=y)
        y += 92

    window.mainloop()


def maths1_current():
    global current_course
    current_course = 'Discrete Mathematics[202101-ACE1312-002]'


def maths2_current():
    global current_course
    current_course = 'Introductory Engineering Mathematics[202101-IGS1130-001]'


def sw_current():
    global current_course
    current_course = 'Software Programming[202101-IGS1131-001]'


def eng_current():
    global current_course
    current_course = 'Business English 2[202101-BUS3002-001]'


def computer_current():
    global current_course
    current_course = 'Computer Programming[202101-IGS1232-001]'

#endregion

def load_course(course_name, window):
    # Destroying the old frame with 5 courses
    global curr_frame
    if curr_frame is not None:
        curr_frame.destroy()


    # Creating a new full white frame
    frame = Frame(window, bg="white", width=1280, height=680)
    frame.place(x=0, y=40)
    curr_frame = frame

    frame_b = LabelFrame(frame, bg = "#005799", width = 1280, height = 80)
    frame_b.place(x = 0, y = 0)

    photo = PhotoImage(file = "images/logo.PNG")

    label = Label(frame, bd = 0, image = photo)
    label.image = photo
    label.place(x = 2, y = 2)



    title = Label(frame, bg = 'white', fg = 'black', text = "User report - UMAROV NURMAKHAMMAD", font = ("Roboto", 28))
    title.place(x = 410, y = 100)


    # Adding style
    style = ttk.Style()
    # Pick a theme
    style.theme_use("alt")
    style.configure(".", font=('Helvetica', 12))
    style.configure("Treeview.Heading", foreground="black", font=('Helvetica', 12, "bold"))
    # Configure our treeview colors
    style.configure("Treeview",
                    background="#f0f0f0",
                    foreground="black",
                    rowheight=33,
                    fieldbackground="#f0f0f0"
                    )

    # Change selected color
    style.map("Treeview",
              background=[("selected", "#3d84b8")])

    # my_tree = ttk.Treeview(frame)
    my_tree = ttk.Treeview(

        frame,
        columns=(1, 2, 3, 4, 5, 6),
        height=13
    )

    # Define our Columns
    my_tree['columns'] = ("Grade item", "Calculated weight", "Grade", "Percentage", "Percentile conversion grade")

    # formate our columns
    my_tree.column("#0", width=0, minwidth=330)
    my_tree.column("Grade item", anchor=CENTER, width=125)
    my_tree.column("Calculated weight", anchor=CENTER, width=130)
    my_tree.column("Grade", anchor=CENTER, width=150)
    my_tree.column("Percentage", anchor=CENTER, width=170)
    my_tree.column("Percentile conversion grade", anchor=CENTER, width=540)
    # formate our headings
    my_tree.heading("#0", text="Grade item", anchor=CENTER)
    my_tree.heading("Grade item", text="Calculated weight", anchor=CENTER)
    my_tree.heading("Calculated weight", text="Grade", anchor=CENTER)
    my_tree.heading("Grade", text="Range", anchor=CENTER)
    my_tree.heading("Percentage", text="Percentage", anchor=CENTER)
    my_tree.heading("Percentile conversion grade", text="Percentile conversion grade", anchor=CENTER)

    # Adding data
    my_tree.insert(parent="", index="end", iid=0, text="Quiz IGS1131-001 Midterm Exam",
                   values=("100.00 %", "65.33", "0–100", "65.33 %", "10.33"))
    my_tree.insert(parent="", index="end", iid=1, text="Σ Total midterms",
                   values=("15.00 % ", "65.33", "0–100", "65.33 %", "10.33"))
    my_tree.insert(parent="", index="end", iid=2, text="Σ Final exam total",
                   values=("15.00 %", "-", "-", "-", "-"))
    my_tree.insert(parent="", index="end", iid=3, text="Σ Total attendance",
                   values=("10.00 %", "10", "0–100", "10%", "10.00"))
    my_tree.insert(parent="", index="end", iid=4, text="Σ Quiz total",
                   values=("10.00 %", "10.00", "0–100", "10%", "10.00"))
    my_tree.insert(parent="", index="end", iid=5, text="Σ Discussion total",
                   values=("10.00 %", "10.00", "0–100", "10%", "10.00"))
    my_tree.insert(parent="", index="end", iid=6, text="Homework-1: Self-Introduction",
                   values=("16.67 %", "100.00", "0–100", "100.00 %", "6.67", "absent"))  # absence
    my_tree.insert(parent="", index="end", iid=7, text="Exercise 3.1, 3.2 & 3.3: Modules and Functions",
                   values=("16.67 %", "100.00", "0–100", "100.00 %", "6.67"))
    my_tree.insert(parent="", index="end", iid=8, text="Exercise 4.2: Recursion Function & Conditionals",
                   values=("16.67 %", "100.00", "0–100", "-", "6.67"))  # absence
    my_tree.insert(parent="", index="end", iid=9, text="Exercise 8.1, 8.2, 8.3 & 8.4: Lists", values=(
    "16.67 %", "100.00", "0–100", "100.00 %", "6.67"))
    my_tree.insert(parent="", index="end", iid=10, text="IGS1131-001 Team Project Proposal Submission Link",
                   values=("16.67 %", "-", "0–100", "-", "-"))
    my_tree.insert(parent="", index="end", iid=11, text="IGS1131-001 Team Project Materials Submission Link", values=(
    "16.67 %", "-", "0–100", "-", "-"))
    my_tree.insert(parent="", index="end", iid=12, text="Σ Course total",
                   values=("-", "244.77", "0–700", "44.87 %", "44.87"))

    # Pack to the screen
    my_tree.place(y=160, x=80)
