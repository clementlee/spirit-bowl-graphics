from Tkinter import *
import tkFont

elp = 0
fresh = 0
soph = 0
jun = 0
sen = 0




root = Tk()
v = IntVar()
elpvar = StringVar()
freshvar = StringVar()
sophvar = StringVar()
junvar = StringVar()
senvar = StringVar()
standard = tkFont.Font(family='Helvetica', size=128, weight='normal')

event = ""
eventvar = StringVar()


control = Toplevel()

elpe = Entry(control)
freshe = Entry(control)
sophe = Entry(control)
june = Entry(control)
sene = Entry(control)

evente = Entry(control)

w, h = root.winfo_screenwidth(), root.winfo_screenheight()

eventframe = Frame(master = root, width=w, height=h, bg="black")
eventframe.pack_propagate(0)
scoreframe = Frame(master = root, width=w, height=h, bg="black")
scoreframe.grid_propagate(0)

Label(master=eventframe, text="NEXT EVENT:", bg="black",\
                   fg="red", font= standard).pack(side = TOP)
eventlabel = Label(master=eventframe, textvariable=eventvar, bg="black",\
                   fg="red", font= standard)
eventlabel.pack(fill=BOTH,expand = True)

c= 100

Label(master=scoreframe, text="SCORES", bg="black",\
                   fg="red", font= standard).grid(row = 0, columnspan = 2)
Label(master=scoreframe, text="ELP", bg="black",\
                   fg="red", font= standard).grid(row = 1, column= 0,padx =c)
Label(master=scoreframe, textvariable=elpvar, bg="black",\
                   fg="red", font= standard).grid(row = 1, column= 1,padx =c)
Label(master=scoreframe, text="Freshmen", bg="black",\
                   fg="red", font= standard).grid(row = 2, column= 0,padx =c)
Label(master=scoreframe, textvariable=freshvar, bg="black",\
                   fg="red", font= standard).grid(row = 2, column= 1,padx =c)
Label(master=scoreframe, text="Sophomores", bg="black",\
                   fg="red", font= standard).grid(row = 3, column= 0,padx =c)
Label(master=scoreframe, textvariable=sophvar, bg="black",\
                   fg="red", font= standard).grid(row = 3, column= 1,padx =c)
Label(master=scoreframe, text="Juniors", bg="black",\
                   fg="red", font= standard).grid(row = 4, column= 0,padx =c)
Label(master=scoreframe, textvariable=junvar, bg="black",\
                   fg="red", font= standard).grid(row = 4, column= 1,padx =c)
Label(master=scoreframe, text="Seniors", bg="black",\
                   fg="red", font= standard).grid(row = 5, column= 0,padx =c)
Label(master=scoreframe, textvariable=senvar, bg="black",\
                   fg="red", font= standard).grid(row = 5, column= 1,padx =c)

def update():
    elp = int(elpe.get())
    fresh = int(freshe.get())
    soph = int(sophe.get())
    jun = int(june.get())
    sen = int(sene.get())
    event = evente.get()
    eventvar.set(event)
    elpvar.set(str(elp))
    freshvar.set(str(fresh))
    sophvar.set(str(soph))
    junvar.set(str(jun))
    senvar.set(str(sen))
    print str(elp)+", "+str(fresh)+", "+str(soph)+", "+str(jun)+", "+str(sen)\
          +", "+event+", "+str(v.get())
    eventframe.pack_forget()
    scoreframe.pack_forget()
    
   
    if v.get() == 1:
        scoreframe.pack(fill=BOTH,expand = True)
        print "scores"
    else:
        eventframe.pack(fill=BOTH,expand = True)
        print "events"
    eventframe.config(width = w, height = h)
    scoreframe.config(width = w, height = h)
        

# make it cover the entire screen

root.overrideredirect(1)
#root.geometry("%dx%d+0+0" % (w, h))

#root.focus_set() # <-- move focus to this widget
root.bind("<Escape>", lambda e: exit())


control.title("Controls")
b = Button(control, text="Update!", command=update)
b.grid(row = 0, columnspan = 2)
b1 = Radiobutton(control, text="Scores", variable=v, value=1)
b2 = Radiobutton(control, text="Event", variable=v, value=2)
b1.grid(row = 0, column = 2)
b2.grid(row = 0, column = 3)
Label(control, text="ELP").grid(row=1)
Label(control, text="Freshmen").grid(row=2)
Label(control, text="Sophomores").grid(row=3)
Label(control, text="Juniors").grid(row=4)
Label(control, text="Seniors").grid(row=5)
Label(control, text="Event").grid(row=1, column=2, rowspan = 5)

elpe.insert(0, "0")
freshe.insert(0, "0")
sophe.insert(0, "0")
june.insert(0, "0")
sene.insert(0, "0")

elpe.grid(row=1, column=1)
freshe.grid(row=2, column=1)
sophe.grid(row=3, column=1)
june.grid(row=4, column=1)
sene.grid(row=5, column=1)
evente.grid(row=1, column=3, rowspan = 5)

root.mainloop()
