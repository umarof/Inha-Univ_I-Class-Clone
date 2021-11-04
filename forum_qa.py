
################################################################
from tkinter import *
from tkinter import messagebox
import posts as pt

curr_frame = None
post_number = 0
content_frame = None
max_post = len(pt.posts)

def widgets(window):
    global post_number
    post_number = 0

    # Create a frame which holds your widgets (buttons etc)
    frame0 = Frame(window, bg = "white", width = 1280, height = 680)
    frame0.place(x = 0, y = 40)
    global curr_frame
    curr_frame = frame0

    frame_b = LabelFrame(frame0, bg = "#005799", width = 1280, height = 80)
    frame_b.place(x = 0, y = 0)

    frame_black = LabelFrame(frame0, bg = "#3D3E42", width = 40, height = 601)
    frame_black.place(x = 0, y = 79)

    photo = PhotoImage(file = "images/logo.PNG")

    label = Label(frame0, bd = 0, image = photo)
    label.image = photo  # keep a reference!
    label.place(x = 2, y = 2)

    title1 = Label(frame0, bg = "#005799", fg = "white", text = "Q&A Forum", font = ("Roboto", 20))
    title1.place(x = 210, y = 19)

    title2 = Label(frame0, bg = "white", text = "Posts", font = ("Roboto", 30))
    title2.place(x = 560, y = 110)

    #Search keyword through posts (question / answer / writer name / date)
    key_entry = Text(frame0, bd = 2, height = 1, width = 12)
    key_entry.place(x = 1110, y = 46)
    btn = Button(frame0, text = "Search", command = lambda: find_keyword(key_entry))
    btn.place(x = 1220, y = 44)

    posts_frame(frame0)



def posts_frame(frame0):
    frame1 = LabelFrame(frame0, bg = "white", width = 980, height = 420)
    frame1.place(x = 140, y = 180)

    #Add new_question button
    _question = Button(frame0, text = "New Question", font = ("Roboto", 12), command = lambda: new_question(frame1))
    _question.place(x = 557, y = 620)

    #region Array Captions
    _fra = LabelFrame(frame1, bg= "white", width=976, height=40)
    _fra.place(x = 0, y = 0)
    _title = Label(_fra,bg = "white", text = "Question", font = ("Roboto", 18))
    _title.place(x = 1, y = 1)
    _message = Label(_fra, bg="white", text="Answer", font=("Roboto", 18))
    _message.place(x = 200, y = 1)
    _writer = Label(_fra, bg="white", text="Writer", font=("Roboto", 18))
    _writer.place(x = 650, y = 1)
    _date = Label(_fra, bg="white", text="Date", font=("Roboto", 18))
    _date.place(x = 870, y = 1)
    #endregion

    display_post(post_number, frame1)


def display_post(number, frame1):
    global content_frame
    if content_frame is not None:
        content_frame.destroy()

    content_frame = LabelFrame(frame1, bg = "white", width = 976, height = 376)
    content_frame.place(x = 0, y = 40)
    global max_post
    if post_number == 0:
        new_question(frame1)
    display_post_nb(frame1)

    # region Prev-Next
    prv = Button(frame1, text="Prev", command = lambda: _prev(frame1))
    prv.place(x = 5, y = 385)
    nxt = Button(frame1, text="Next", command = lambda : _nxt(frame1))
    nxt.place(x = 935, y = 385)
    # endregion

    #Will display every information of a post (Question/Answer/...)
    if pt.posts.get(str(post_number)) is not None :
        display_question(number)
        display_answer(number)
        display_writer(number)
        display_date(number)

def display_question(number):
    st_question = pt.posts.get(str(number))[0]
    new_line(st_question, 5, 15)

def display_answer(number):
    st_answer = pt.posts.get(str(number))[1]
    #If question has not been answered, it is possible to answer it.
    if st_answer == "":
        ent2 = Text(content_frame, bd = 4, height = 17, width = 40)
        ent2.place(x = 212, y = 10)
        # Add answer_question button
        _answer = Button(content_frame, text = "Answer Question", font = ("Roboto", 10),
                         command = lambda: get_entries(ent2))
        _answer.place(x = 813, y = 341)
    new_line(st_answer, 200, 40)

def display_writer(number):
    st_writer = pt.posts.get(str(number))[2]
    new_line(st_writer, 650, 15)

def display_date(number):
    st_date = pt.posts.get(str(number))[3]
    new_line(st_date, 870, 5)

def display_post_nb(frame1):
    #Display post number
    post_nb = LabelFrame(frame1, bg = "grey", width = 30, height = 30)
    post_nb.place(x = 460, y = 370)
    _nb = Label(post_nb, bg = "grey", fg = "white", text = str(post_number), font = ("Calibri", 12))
    _nb.place(x = 5, y = 0)

#Very basic function that just display max_char on 1 line and increment _y (newline behaviour)
def new_line(st_message, _x, max_char):
    global content_frame
    _y = 5
    st_temp = ""
    for i in range(1, len(st_message) + 1):
        curr_char = st_message[i - 1]
        #Remove space at beginning of a line
        if i % max_char == 1 and  curr_char == " ":
            continue
        st_temp += curr_char
        #Every max_char char stored in st_temp are printed on the GUI.
        if i % max_char == 0:
            _message = Label(content_frame, bg = "white", text = st_temp, font = ("Roboto", 16))
            _message.place(x = _x, y = _y)
            st_temp = ""
            #Move y position (same job as newline)
            _y += 30
    #As the string is cut in (max_char) char parts, if last part is less than (max_char) char, it won't be displayed.
    _message = Label(content_frame, bg = "white", text = st_temp, font = ("Roboto", 16))
    _message.place(x = _x, y = _y)

#For prv button
def _prev(frame1):
    global post_number
    if post_number > 1:
        post_number -= 1
        if pt.posts.get(str(post_number)) is not None:
            display_post(post_number, frame1)

#For nxt button
def _nxt(frame1):
    global post_number
    if pt.posts.get(str(post_number + 1)) is not None:
        post_number += 1
        display_post(post_number, frame1)

#Destroy post frame if there is one currently displayed + call display_post with argument 0 to create a post frame but
#doesnt display any post (as given number is 0, however, minimum index for a post is 1) + display entry spaces.
def new_question(frame1):
    if content_frame is not None:
        content_frame.destroy()

    global post_number
    post_number = max_post + 1
    display_post(0, frame1)
    display_entries()

#Cretae widgets for the creation of a new post
def display_entries():
    ent1 = Text(content_frame, bd = 4, height = 17, width = 20)
    ent1.place(x = 3, y = 10)

    ent2 = Text(content_frame, bd = 4, height = 17, width = 40)
    ent2.place(x = 202, y = 10)

    ent3 = Text(content_frame, bd = 4, height = 17, width = 20)
    ent3.place(x = 652, y = 10)

    ent4 = Text(content_frame, bd = 4, height = 17, width = 10)
    ent4.place(x = 872, y = 10)

    _save = Button(content_frame, text = "Post it", font = ("Roboto", 10), command = lambda: get_entries(ent2, ent1, ent3, ent4))
    _save.place(x = 875, y = 341)


#Get the input entries and write to the posts.py file only if user writes Question + his Name + Date
def get_entries(ent2, ent1 = None, ent3 = None, ent4 = None):
    st1 = ""
    st2 = ent2.get("1.0", 'end-1c')
    st3 = ""
    st4 = ""
    if ent1 is not None and ent3 is not None and ent4 is not None:
        st1 = ent1.get("1.0", 'end-1c')
        st3 = ent3.get("1.0", 'end-1c')
        st4 = ent4.get("1.0", 'end-1c')

    file = open("posts.py", 'w')

    #Update posts with at least question, writer and date
    if st1 != "" and st3 != "" and st4 != "":
        pt.posts.update({str(post_number):[st1, st2, st3, st4]})
        file.write("%s = %s\n" %("posts", pt.posts))
        global max_post
        max_post += 1

        messagebox.showinfo('Posted', '     Your question has been posted.\nPlease refresh the forum to see your post.')
    #Update posts file with the answer
    elif ent1 is None and st2 != "":
        pt.posts.get(str(post_number))[1] = st2
        file.write("%s = %s\n" % ("posts", pt.posts))
        messagebox.showinfo('Answered', '          Question has been answered.\nPlease refresh the forum to see your answer.')
    else:
        file.write("%s = %s\n" % ("posts", pt.posts))

    file.close()


def badCharHeuristic(string, size):
    badChar = [-1] * 256

    for i in range(size):
        badChar[ord(string[i])] = i;

    return badChar


def search(txt, pat):
    m = len(pat)
    n = len(txt)

    badChar = badCharHeuristic(pat, m)
    s = 0
    while s <= n - m:
        j = m - 1

        while j >= 0 and pat[j] == txt[s + j]:
            j -= 1

        if j < 0:
            #print("Pattern occur at shift = {}".format(s))

            s += (m - badChar[ord(txt[s + m])] if s + m < n else 1)
            return True
        else:
            s += max(1, j - badChar[ord(txt[s + j])])
    return False

def find_keyword(key_entry):
    pat = key_entry.get("1.0", 'end-1c')
    if pat != "":
        st = ""
        for k,v in pt.posts.items():
            if v:
                if search(v[0], pat):
                    st += k + " -> Question\n"
                if search(v[1], pat):
                    st += k + " -> Answer\n"
                if search(v[2], pat):
                    st += k + " -> Writer\n"
                if search(v[3], pat):
                    st += k + " -> Date\n"
        if st == "":
            messagebox.showinfo(":(", "Nothing found !")
        else:
            messagebox.showinfo(":)", st)