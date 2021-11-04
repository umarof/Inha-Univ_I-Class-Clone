
from tkinter import *
from tkinter import messagebox
import database as db
from tkinter import ttk

curr_frame = None
current_course = None
course_code = None
division_code = None
content_frame = None

#region DO NOT TOUCH
def widgets(window):
    # Creating new frame and updating the current frame
    frame = Frame(window, bg="#005799", width=1280, height=680)
    frame.place(x = 0, y = 40)

    global curr_frame
    curr_frame = frame

    title = Label(frame, bg = '#005799', fg = 'white', text = "Course Attendance", font = ("Roboto", 40))
    title.place(x = 410, y = 20)

    courses = ['maths1', 'sw', 'maths2', 'computer', 'eng']
    images_and_names = []
    for c in courses:
        img = PhotoImage(file = 'images/img_' + c + '.png', master = frame)
        images_and_names.append((img, c))

    buttons = []
    for i in images_and_names:
        t = i[1]
        if t == 'sw':
            btn = Button(frame, image=i[0], command=lambda: [sw_current(), load_course(window)], height=92,
                         width=911)
            btn.image = i[0]
        elif t == 'maths1':
            btn = Button(frame, image=i[0], command=lambda: [maths1_current(), load_course(window)], height=92,
                         width=911)
            btn.image = i[0]
        elif t == 'maths2':
            btn = Button(frame, image=i[0], command=lambda: [maths2_current(), load_course(window)], height=92,
                         width=911)
            btn.image = i[0]
        elif t == 'computer':
            btn = Button(frame, image=i[0], command=lambda: [computer_current(), load_course(window)], height=92,
                         width=911)
            btn.image = i[0]
        elif t == 'eng':
            btn = Button(frame, image=i[0], command=lambda: [eng_current(), load_course(window)], height=92,
                         width=911)
            btn.image = i[0]
        else:
            btn = Button(frame, image=i[0], command=lambda: load_course(window), height=92, width=911)
        buttons.append(btn)

    y = 110
    for b in buttons:
        b.place(x=184, y=y)
        y += 92


def maths1_current():
    global current_course, course_code, division_code
    current_course = 'Discrete Mathematics[202101-ACE1312-002]'
    course_code = 'ACE1312'
    division_code = '002'

def maths2_current():
    global current_course, course_code, division_code
    current_course = 'Introductory Engineering Mathematics[202101-IGS1130-001]'
    course_code = 'IGS1130'
    division_code = '001'

def sw_current():
    global current_course, course_code, division_code
    current_course = 'Software Programming[202101-IGS1131-001]'
    course_code = 'IGS1131'
    division_code = '001'

def eng_current():
    global current_course, course_code, division_code
    current_course = 'Business English 2[202101-BUS3002-001]'
    course_code = 'BUS3002'
    division_code = '001'

def computer_current():
    global current_course, course_code, division_code
    current_course = 'Computer Programming[202101-IGS1232-001]'
    course_code = 'IGS1232'
    division_code = '001'

#endregion

def load_course(window):
    #region Dm stuff
    # Destroying the old frame with 5 courses
    global curr_frame
    if curr_frame is not None:
        curr_frame.destroy()

    # Creating a new full white frame
    frame = Frame(window, bg = "white", width = 1280, height = 680)
    frame.place(x = 0, y = 40)
    curr_frame = frame

    # Top frame with the course title
    blue_frame = LabelFrame(frame, bg = "#005799", width = 1280, height = 80)
    blue_frame.place(x = 0, y = 0)
    title = Label(blue_frame, bg = '#005799', fg = 'white', text = current_course, font = ("Roboto", 20))
    title.place(x = 210, y = 18)
    #endregion

    photo = PhotoImage(file = "images/logo.PNG")

    label = Label(blue_frame, bd = 0, image = photo)
    label.image = photo  # keep a reference!
    label.place(x = 2, y = 2)

    left_frame = LabelFrame(frame, bg = "white", width = 190, height = 600)
    left_frame.place(x = 0, y = 79)
    grey_frame = LabelFrame(left_frame, text = "Attendance", bg = "#f0f0f0", width = 150, height = 150,
                            font = ("Roboto", 14, "bold"))
    grey_frame.place(x = 10, y = 8)



    btn1 = Button(grey_frame, bd = 1, text = "Offline Attendance", font = ("Roboto", 11),
                  command = lambda: display_offline(frame))
    btn1.place(x = 4, y = 10)

    btn2 = Button(grey_frame, bd = 1, text = "Online Attendance", font = ("Roboto", 11),
                  command = lambda: display_online(frame))
    btn2.place(x = 4, y = 50)



def display_offline(frame):
    global content_frame
    if content_frame is not None:
        content_frame.destroy()
    content_frame = LabelFrame(frame, bg = "white", width = 1090, height = 600)
    content_frame.place(x = 192, y = 79)

    #region head_frame
    head_frame = LabelFrame(content_frame, bg = "white", width = 1075, height = 70)
    head_frame.place(x = 5, y = 30)
    cs_code = Label(head_frame, bg = "white", text = "Course Code : " + course_code, font = ("Roboto", 13))
    cs_code.place(x = 5, y = 18)
    cs_name = Label(head_frame, bg = "white", text = "Course Name : " + current_course, font = ("Roboto", 12))
    cs_name.place(x = 240, y = 18)
    cs_code = Label(head_frame, bg = "white", text = "Division Code : " + division_code, font = ("Roboto", 13))
    cs_code.place(x = 840, y = 18)
    #endregion

    #region captions
    week_caption = LabelFrame(content_frame, bg = "white", width = 200, height = 30)
    week_caption.place(x = 40, y = 109)
    week_text = Label(week_caption, bg = "white", text = "Week", font = ("Roboto", 11))
    week_text.place(x = 75, y = 1)

    class_caption = LabelFrame(content_frame, bg=  "white", width = 200, height = 30)
    class_caption.place(x = 235, y = 109)
    class_text = Label(class_caption, bg = "white", text = "Class", font = ("Roboto", 11))
    class_text.place(x = 75, y = 1)

    attendance_caption = LabelFrame(content_frame, bg = "white", width = 200, height = 30)
    attendance_caption.place(x = 430, y = 109)
    attendance_text = Label(attendance_caption, bg = "white", text = "Attendance", font = ("Roboto", 11))
    attendance_text.place(x = 60, y = 1)

    absence_caption = LabelFrame(content_frame, bg = "white", width = 200, height = 30)
    absence_caption.place(x = 625, y = 109)
    absence_text = Label(absence_caption, bg = "white", text = "Absence", font = ("Roboto", 11))
    absence_text.place(x = 65, y = 1)

    late_caption = LabelFrame(content_frame, bg = "white", width = 200, height = 30)
    late_caption.place(x = 820, y = 109)
    late_text = Label(late_caption, bg = "white", text = "Late", font = ("Roboto", 11))
    late_text.place(x = 75, y = 1)
    #endregion

    _y = 140
    db_course = db.courses.get(current_course)
    db_attendance = db.students.get("12210420")[8].get(current_course)
    _att = 0
    _abs = 0
    _lt = 0
    if db_attendance is not None and db_course is not None:
        for i in range(12):
            _week = LabelFrame(content_frame, bg = "white", width = 200, height = 30)
            _week.place(x = 40, y = _y)
            txt_week = Label(_week, bg = "white", text = db_course[i], font = ("Roboto", 11))
            txt_week.place(x = 55, y = 1)

            _class = LabelFrame(content_frame, bg = "white", width = 200, height = 30)
            _class.place(x = 235, y = _y)
            txt_class = Label(_class, bg = "white", text = str(i + 1), font = ("Roboto", 11))
            if i < 9:
                txt_class.place(x = 90, y = 1)
            else:
                txt_class.place(x = 86, y = 1)

            _attendance = LabelFrame(content_frame, bg = "white", width = 200, height = 30)
            _attendance.place(x = 430, y = _y)
            if db_attendance[i] == 0:
                _att += 1
                txt_attendance = Label(_attendance, bg = "white", text = "O", font = ("Roboto", 11))
                txt_attendance.place(x = 88, y = 1)

            _absence = LabelFrame(content_frame, bg = "white", width = 200, height = 30)
            _absence.place(x = 625, y = _y)
            if db_attendance[i] == 1:
                _abs += 1
                txt_absence = Label(_absence, bg = "white", text = "O", font = ("Roboto", 11))
                txt_absence.place(x = 88, y = 1)

            _late = LabelFrame(content_frame, bg = "white", width = 200, height = 30)
            _late.place(x = 820, y = _y)
            if db_attendance[i] == 2:
                _lt += 1
                txt_late = Label(_late, bg = "white", text = "O", font = ("Roboto", 11))
                txt_late.place(x = 88, y = 1)

            _y += 28
    else:
        messagebox.showinfo(':(', 'Nothing found')

    # region Attendance summary
    summary_frame = LabelFrame(content_frame, width=600, height=30)
    summary_frame.place(x=20, y=500)
    txt_summary = Label(summary_frame, text="Attendance : " + str(_att) + ", Absence : " + str(_abs)
                                                + ", Late : " + str(_lt), font=("Roboto", 11))
    txt_summary.place(x=5, y=2)
    # endregion



# Displaying online attendance for Software Programming

def display_online(frame):
    global content_frame
    if content_frame is not None:
        content_frame.destroy()
    content_frame = LabelFrame(frame, bg = "white", width = 1090, height = 600)
    content_frame.place(x = 192, y = 79)

    # head_frame
    head_frame = LabelFrame(content_frame, bg = "white", width = 1075, height = 70)
    head_frame.place(x = 5, y = 30)
    cs_code = Label(head_frame, bg = "white", text = "Course Code : " + course_code, font = ("Roboto", 13))
    cs_code.place(x = 5, y = 18)
    cs_name = Label(head_frame, bg = "white", text = "Course Name : " + current_course, font = ("Roboto", 12))
    cs_name.place(x = 240, y = 18)
    cs_code = Label(head_frame, bg = "white", text = "Division Code : " + division_code, font = ("Roboto", 13))
    cs_code.place(x = 840, y = 18)


    # Adding style
    style = ttk.Style()
    # Pick a theme
    style.theme_use("alt")
    style.configure(".", font=('Helvetica', 12))
    style.configure("Treeview.Heading", foreground="black", font=('Helvetica', 12, "bold"))
    # Configure our treeview colors
    style.configure("Treeview",
                    background = "#f0f0f0",
                    foreground = "black",
                    rowheight = 33,
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
    my_tree['columns'] = ("Name", "Required time", "Watched time", "Attendance", "Absence")

    # formate our columns
    my_tree.column("#0", width=0, minwidth=50)
    my_tree.column("Name", anchor=W, width=515)
    my_tree.column("Required time", anchor=CENTER, width=120,)
    my_tree.column("Watched time", anchor=CENTER, width=120)
    my_tree.column("Attendance", anchor=CENTER, width=100)
    my_tree.column("Absence", anchor=CENTER, width=140)
    # formate our headings
    my_tree.heading("#0", text="WEEKS", anchor=CENTER)
    my_tree.heading("Name", text=" LECTURE VODs", anchor=CENTER)
    my_tree.heading("Required time", text="Required", anchor=CENTER)
    my_tree.heading("Watched time", text="Watched", anchor=CENTER)
    my_tree.heading("Attendance", text="Attendance", anchor=CENTER)
    my_tree.heading("Absence", text="Absence", anchor=CENTER)



    # Adding data
    my_tree.insert(parent="", index="end", iid=0, text="1", values=("VOD[ZOOM_REC] IGS1131 Week-1 Lecture", "1:40:00", "1:48:00", "O"))
    my_tree.insert(parent="", index="end", iid=1, text="2", values=("VOD [ZOOM_REC] IGS1131 Week-2 Lecture ", "1:45:00", "1:45:00", "O"))
    my_tree.insert(parent="", index="end", iid=2, text="3", values=("VOD[ZOOM_REC] IGS1131 Week-3 Lecture ", "1:33:00", "1:28:00", "X", "absent"))
    my_tree.insert(parent="", index="end", iid=3, text="4", values=("VOD[ZOOM_REC] IGS1131 Week-4 Lecture ", "1:36:00", "1:45:00", "O"))
    my_tree.insert(parent="", index="end", iid=4, text="5", values=("VOD[ZOOM_REC] IGS1131 Week-5 Lecture ", "1:40:00", "1:45:00", "O"))
    my_tree.insert(parent="", index="end", iid=5, text="6", values=("VOD[ZOOM_REC] IGS1131 Week-6 Lecture ", "1:50:00", "1:45:00", "O"))
    my_tree.insert(parent="", index="end", iid=6, text="7", values=("VOD[ZOOM_REC] IGS1131 Week-7 Lecture", "1:40:00", "1:20:00", "X", "absent")) #absence
    my_tree.insert(parent="", index="end", iid=7, text="8", values=("VOD[ZOOM_REC] IGS1131 Week-8 Lecture", "1:40:00", "1:45:00", "O"))
    my_tree.insert(parent="", index="end", iid=8, text="9", values=("VOD[ZOOM_REC] IGS1131 Week-9 Lecture", "1:40:00", "1:10:00", "X", "absent")) # absence
    my_tree.insert(parent="", index="end", iid=9, text="10", values=("VOD[ZOOM_REC] IGS1131 Week-10 Team Project Briefing & Midterm Exam Detail", "1:50:00", "1:52:00", "O"))
    my_tree.insert(parent="", index="end", iid=10, text="11", values=("VOD[ZOOM_REC]IGS1131 Week-11 Lecture ", "1:43:00", "1:45:00", "O"))
    my_tree.insert(parent="", index="end", iid=11, text="12", values=("VOD[ZOOM_REC] IGS1131 Week-12 Team Project Proposal Presentation Session", "1:54:00", "1:58:00", "O"))
    my_tree.insert(parent="", index="end", iid=12, text="13", values=("VOD[ZOOM_REC] IGS1131 Week-13 Lecture ", "1:36:00", "1:45:00", "O"))

    # Pack to the screen
    my_tree.place(y=185, x=230)



