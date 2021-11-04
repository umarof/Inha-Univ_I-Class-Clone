################################################################

# TO DO:
# Add to login_ops.py : once you click on display_forum, display_grades, log_out,
# display_att or display_mod , you should delete the frame of the course module 
# (csmod.current_frame = None)

from tkinter import *
from tkinter import PhotoImage
import attendance as a
import grades as g

current_frame = None
current_course = None

def widgets(window):
    # Creating new frame and updating the current frame

    frame = Frame(window, bg = "#005799", width = 1280, height = 680)
    frame.place(x = 0, y = 40)
    global current_frame
    current_frame = frame
    
    # Title frame
    title = Label(frame, bg = '#005799', fg = 'white', text = "Course Modules", font = ("Roboto", 40))
    title.place(x = 440, y = 20)
    
    courses = ['maths1', 'sw', 'maths2', 'computer', 'eng']
    images_and_names = []
    for c in courses:
        img = PhotoImage(file = 'images/img_' + c + '.png', master = frame)
        images_and_names.append((img, c))
        
    buttons = []
    for i in images_and_names:
        t = i[1]
        if (t == 'sw'):
            btn = Button(frame, image = i[0], command = lambda:[sw_current(), load_course(i[1], window)], height = 92, width = 911)
        elif (t == 'maths1'):
            btn = Button(frame, image = i[0], command = lambda:[maths1_current(), load_course(i[1], window)], height = 92, width = 911)
        elif (t == 'maths2'):
            btn = Button(frame, image = i[0], command = lambda:[maths2_current(), load_course(i[1], window)], height = 92, width = 911)
        elif (t == 'computer'):
            btn = Button(frame, image = i[0], command = lambda:[computer_current(), load_course(i[1], window)], height = 92, width = 911)
        elif (t == 'eng'):
            btn = Button(frame, image = i[0], command = lambda:[eng_current(), load_course(i[1], window)], height = 92, width = 911)
        else:
            btn = Button(frame, image = i[0], command = lambda:load_course('Course', window), height = 92, width = 911)
        buttons.append(btn)
        
    y = 110
    for b in buttons:
        b.place(x = 184, y = y)
        y += 92
        
    window.mainloop()
    return frame
    
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
    
def load_course(course_name, window):
    # Destroying the old frame with 5 courses
    global current_frame
    if (current_frame != None):
        current_frame.destroy()
    
    # Creating a new full white frame
    frame = Frame(window, bg = "white", width = 1280, height = 680)
    frame.place(x = 0, y = 40)
    current_frame = frame
    
    # Top frame with the course title
    blue_frame = LabelFrame(frame, bg = "#005799", width = 1280, height = 80)
    blue_frame.place(x = 0, y = 0)
    title = Label(blue_frame, bg = '#005799', fg = 'white', text = current_course, font = ("Roboto", 20))
    title.place(x = 210, y = 18)

    photo = PhotoImage(file = "images/logo.PNG")

    label = Label(blue_frame, bd = 0, image = photo)
    label.image = photo  # keep a reference!
    label.place(x = 2, y = 2)
    
    # Page of the course
    if (current_course == 'Discrete Mathematics[202101-ACE1312-002]'):
        img = PhotoImage(file = 'images/maths1.png', master = frame)
        b1 = Button(frame, text="Attendance", command=lambda: [a.maths1_current(), a.load_course(window)], height=2,
               width=21)
        #b1 = Button(frame, text = "Online Attendance", command = lambda:[a.maths1_current(), a.load_course(window)], height = 2, width = 21)
        #b2 = Button(frame, text = "Offline Attendance", command = lambda:[a.maths1_current(), a.load_course(window)], height = 2, width = 21)
        b3 = Button(frame, text = "Grades", command = lambda:[g.maths1_current(), g.load_course('maths1', window)], height = 2, width = 21)
    elif (current_course == 'Introductory Engineering Mathematics[202101-IGS1130-001]'):
        img = PhotoImage(file = 'images/maths2.png', master = frame)
        b1 = Button(frame, text="Attendance", command=lambda: [a.maths2_current(), a.load_course(window)],
                    height=2, width=21)
        #b1 = Button(frame, text = "Online Attendance", command = lambda:[a.maths2_current(), a.load_course(window)], height = 2, width = 21)
        #b2 = Button(frame, text = "Offline Attendance", command = lambda:[a.maths2_current(), a.load_course(window)], height = 2, width = 21)
        b3 = Button(frame, text = "Grades", command = lambda:[g.maths1_current(), g.load_course('maths2', window)], height = 2, width = 21)
    elif (current_course == 'Software Programming[202101-IGS1131-001]'):
        img = PhotoImage(file = 'images/sw.png', master = frame)
        b1 = Button(frame, text="Attendance", command=lambda: [a.sw_current(), a.load_course(window)], height=2,
                    width=21)
        #b1 = Button(frame, text = "Online Attendance", command = lambda:[a.sw_current(), a.load_course(window)], height = 2, width = 21)
        #b2 = Button(frame, text = "Offline Attendance", command = lambda:[a.sw_current(), a.load_course(window)], height = 2, width = 21)
        b3 = Button(frame, text = "Grades", command = lambda:[g.maths1_current(), g.load_course('sw', window)], height = 2, width = 21)
    elif (current_course == 'Business English 2[202101-BUS3002-001]'):
        img = PhotoImage(file = 'images/eng.png', master = frame)
        b1 = Button(frame, text="Attendance", command=lambda: [a.eng_current(), a.load_course(window)], height=2,
                    width=21)
        #b1 = Button(frame, text = "Online Attendance", command = lambda:[a.eng_current(), a.load_course(window)], height = 2, width = 21)
        #b2 = Button(frame, text = "Offline Attendance", command = lambda:[a.eng_current(), a.load_course('eng', window)], height = 2, width = 21)
        b3 = Button(frame, text = "Grades", command = lambda:[g.maths1_current(), g.load_course('eng', window)], height = 2, width = 21)
    else:
        img = PhotoImage(file = 'images/computer.png', master = frame)
        b1 = Button(frame, text="Attendance", command=lambda: [a.computer_current(), a.load_course(window)],
                    height=2, width=21)
        #b1 = Button(frame, text = "Online Attendance", command = lambda:[a.computer_current(), a.load_course(window)], height = 2, width = 21)
        #b2 = Button(frame, text = "Offline Attendance", command = lambda:[a.computer_current(), a.load_course(window)], height = 2, width = 21)
        b3 = Button(frame, text = "Grades", command = lambda:[g.maths1_current(), g.load_course('computer', window)], height = 2, width = 21)
    
    label = Label(image = img)
    label.image = img
    label.place(x = 35, y = 200)
    
    b1.place(x = 35, y = 100)
    #b2.place(x = 210, y = 100)
    b3.place(x = 199, y = 100)
    
    #window.mainloop()
    
    
