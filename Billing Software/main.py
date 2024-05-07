from tkinter import *
from tkinter import messagebox

def login():
    user=username.get()
    code=password.get()
    if user=="sudhar" and code=="123":
        root=Toplevel(screen)
        root.title("Bill")
        root.geometry("1280x720+150+80")
        root.configure(bg="#d7dae2")
        root.resizable(False,False)
        def Reset():
            entry_dosa.delete(0, END)
            entry_itlee.delete(0, END)
            entry_pongal.delete(0, END)
            entry_Barrota.delete(0, END)
            entry_Poori.delete(0, END)
            entry_Paniyaram.delete(0, END)
            entry_Chapathi.delete(0, END)
            entry_Tea.delete(0, END)
            entry_Cofee.delete(0, END)

        def Total():
            print()
            try:
                a1 = int(Dosa.get())
            except:
                a1 = 0

            try:
                a2 = int(Itlee.get())
            except:
                a2 = 0

            try:
                a3 = int(Pongal.get())
            except:
                a3 = 0

            try:
                a4 = int(Barrota.get())
            except:
                a4 = 0

            try:
                a5 = int(Poori.get())
            except:
                a5 = 0

            try:
                a6 = int(Paniyaram.get())
            except:
                a6 = 0

            try:
                a7 = int(Chapathi.get())
            except:
                a7 = 0

            try:
                a8 = int(Tea.get())
            except:
                a8 = 0

            try:
                a9 = int(Cofee.get())
            except:
                a9 = 0

            # Define amounr per quantity

            c1 = 60 * a1
            c2 = 40 * a2
            c3 = 50 * a3
            c4 = 20 * a4
            c5 = 30 * a5
            c6 = 70 * a6
            c7 = 10 * a7
            c8 = 12 * a8
            c9 = 18 * a9

            lbl_total = Label(f2, font=("aria", 20, "bold"), text="Total", width=16, fg="lightyellow", bg="black")
            lbl_total.place(x=0, y=50)

            entry_total = Entry(f2, font=("aria", 20, "bold"), textvariable=Total_bill, bd=6, width=15, bg="lightgreen")
            entry_total.place(x=20, y=100)

            totalcost = c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8 + c9
            string_bill = "Rs.", str("%.2f" % totalcost)
            Total_bill.set(string_bill)

        Label(root,text="Bill Management", bg="black", fg="white", font=("calibri", 33), width="300", height="2").pack()

        # welcome card
        w = Frame(root, bg="green", highlightbackground="black", highlightthickness=1, width=300, height=70)
        w.place(x=10, y=120)
        Label(w, text="WELCOME", font=("aria", 20, "bold"), bg="white").place(x=70, y=11)

        # menu card
        f = Frame(root, bg="lightgreen", highlightbackground="black", highlightthickness=1, width=300, height=370)
        f.place(x=10, y=175)
        # menu card content
        Label(f, text="Menu", font=("Gabriola", 30, "bold"), fg="black", bg="lightgreen").place(x=100, y=0)
        Label(f, text="Dosa.......Rs.60/plate", font=("Lucida calligraphy", 10, "bold"), fg="black",
              bg="lightgreen").place(
            x=60, y=80)
        Label(f, text="Itlee......Rs.40/plate", font=("Lucida calligraphy", 10, "bold"), fg="black",
              bg="lightgreen").place(
            x=60, y=110)
        Label(f, text="Pongal.....Rs.50/plate", font=("Lucida calligraphy", 10, "bold"), fg="black",
              bg="lightgreen").place(
            x=60, y=140)
        Label(f, text="Barrota....Rs.20/plate", font=("Lucida calligraphy", 10, "bold"), fg="black",
              bg="lightgreen").place(
            x=60, y=170)
        Label(f, text="Poori......Rs.30/plate", font=("Lucida calligraphy", 10, "bold"), fg="black",
              bg="lightgreen").place(
            x=60, y=200)
        Label(f, text="Chapathi...Rs.70/plate", font=("Lucida calligraphy", 10, "bold"), fg="black",
              bg="lightgreen").place(
            x=60, y=230)
        Label(f, text="Paniyaram..Rs.10/plate", font=("Lucida calligraphy", 10, "bold"), fg="black",
              bg="lightgreen").place(
            x=60, y=260)
        Label(f, text="Tea........Rs.12/", font=("Lucida calligraphy", 10, "bold"), fg="black", bg="lightgreen").place(
            x=60,
            y=290)
        Label(f, text="Cofee......Rs.18/", font=("Lucida calligraphy", 10, "bold"), fg="black", bg="lightgreen").place(
            x=60,
            y=320)
        # bill
        f2 = Frame(root, bg="lightyellow", highlightbackground="black", highlightthickness=1, width=300, height=420)
        f2.place(x=950, y=118)
        bill = Label(f2, text="Bill", font=("callibri", 20), bg="lightyellow")
        bill.place(x=120, y=10)

        # Entry Work
        f1 = Frame(root, bd=5, height=400, width=300, relief=RAISED)
        f1.pack()

        Dosa = StringVar()
        Itlee = StringVar()
        Pongal = StringVar()
        Barrota = StringVar()
        Poori = StringVar()
        Paniyaram = StringVar()
        Chapathi = StringVar()
        Tea = StringVar()
        Cofee = StringVar()
        Total_bill = StringVar()

        # label
        lbl_dosa = Label(f1, font=("aria", 20, "bold"), text="Dosa", width=12, fg="blue4")
        lbl_Itlee = Label(f1, font=("aria", 20, "bold"), text="Itlee", width=12, fg="blue4")
        lbl_Pongal = Label(f1, font=("aria", 20, "bold"), text="Pongal", width=12, fg="blue4")
        lbl_Barrota = Label(f1, font=("aria", 20, "bold"), text="Barrota", width=12, fg="blue4")

        lbl_Poori = Label(f1, font=("aria", 20, "bold"), text="Poori", width=12, fg="blue4")
        lbl_Chapathi = Label(f1, font=("aria", 20, "bold"), text="Chapathi", width=12, fg="blue4")
        lbl_Paniyaram = Label(f1, font=("aria", 20, "bold"), text="Paniyaram", width=12, fg="blue4")
        lbl_Tea = Label(f1, font=("aria", 20, "bold"), text="Tea", width=12, fg="blue4")
        lbl_Cofee = Label(f1, font=("aria", 20, "bold"), text="Cofee", width=12, fg="blue4")

        lbl_dosa.grid(row=1, column=0)
        lbl_Itlee.grid(row=2, column=0)
        lbl_Pongal.grid(row=3, column=0)
        lbl_Barrota.grid(row=4, column=0)
        lbl_Poori.grid(row=5, column=0)
        lbl_Chapathi.grid(row=6, column=0)
        lbl_Paniyaram.grid(row=7, column=0)
        lbl_Tea.grid(row=8, column=0)
        lbl_Cofee.grid(row=9, column=0)

        # entry
        entry_dosa = Entry(f1, font=("aria", 20, "bold"), textvariable=Dosa, bd=6, width=8, bg="lightpink")
        entry_dosa.grid(row=1, column=1)
        entry_itlee = Entry(f1, font=("aria", 20, "bold"), textvariable=Itlee, bd=6, width=8, bg="lightpink")
        entry_itlee.grid(row=2, column=1)
        entry_pongal = Entry(f1, font=("aria", 20, "bold"), bd=6, width=8, textvariable=Pongal, bg="lightpink")
        entry_pongal.grid(row=3, column=1)
        entry_Barrota = Entry(f1, font=("aria", 20, "bold"), textvariable=Barrota, bd=6, width=8, bg="lightpink")
        entry_Barrota.grid(row=4, column=1)
        entry_Poori = Entry(f1, font=("aria", 20, "bold"), textvariable=Poori, bd=6, width=8, bg="lightpink")
        entry_Poori.grid(row=5, column=1)
        entry_Paniyaram = Entry(f1, font=("aria", 20, "bold"), textvariable=Paniyaram, bd=6, width=8, bg="lightpink")
        entry_Paniyaram.grid(row=6, column=1)
        entry_Chapathi = Entry(f1, font=("aria", 20, "bold"), textvariable=Chapathi, bd=6, width=8, bg="lightpink")
        entry_Chapathi.grid(row=7, column=1)
        entry_Tea = Entry(f1, font=("aria", 20, "bold"), textvariable=Tea, bd=6, width=8, bg="lightpink")
        entry_Tea.grid(row=8, column=1)
        entry_Cofee = Entry(f1, font=("aria", 20, "bold"), textvariable=Cofee, bd=6, width=8, bg="lightpink")
        entry_Cofee.grid(row=9, column=1)

        # welcome card
        w = Frame(root, bg="green", highlightbackground="black", highlightthickness=1, width=300, height=70)
        w.place(x=10, y=120)
        Label(w, text="WELCOME", font=("aria", 20, "bold"), bg="white").place(x=70, y=11)

        # Entry Work
        f1 = Frame(root, bd=5, height=400, width=300, relief=RAISED)
        f1.pack()

        # buttons
        btn_reset = Button(f1, text="Reset", bd=5, font=("aria", 16, "bold"), bg="lightblue", fg="black", width=10,
                           command=Reset)
        btn_reset.grid(row=10, column=0)

        btn_total = Button(f1, text="Total", bd=5, font=("aria", 16, "bold"), bg="lightblue", width=10, command=Total)
        btn_total.grid(row=10, column=1)

    elif user=="" and code=="":
        messagebox.showerror("Invalid","please enter username and password")
    elif user=="":
        messagebox.showerror("invalid","Please enter username currectly")
    elif code=="":
        messagebox.showerror("invalid","Please enter password currectly")
    elif user != "sudhar" and code != "123":
        messagebox.showerror("Invalid", "username and password")

def main_screen():
    global screen
    global username
    global password
    screen = Tk()
    screen.geometry("1280x720+150+80")
    screen.configure(bg="#d7dae2")

    # icon
    image_icon = PhotoImage(file="login.png")
    screen.iconphoto(False, image_icon)
    screen.title("Login system")

    lbTitle = Label(text="Login System", font=("arial", 50, "bold"), fg="black", bg="#d7dae2")
    lbTitle.pack(pady=50)

    bordercolor = Frame(screen, bg="black", width=800, height=400)
    bordercolor.pack()

    mainframe = Frame(bordercolor, bg="#d7dae2", width=800, height=400)
    mainframe.pack(padx=20, pady=20)

    Label(mainframe, text="Username", font=("arial", 30, "bold"), bg="#d7dae2").place(x=100, y=50)
    Label(mainframe, text="Password", font=("arial", 30, "bold"), bg="#d7dae2").place(x=100, y=150)

    username = StringVar()
    password = StringVar()
    entry_username = Entry(mainframe, textvariable=username, width=12, bd=2, font=("arial", 30))
    entry_username.place(x=400, y=50)
    entry_password = Entry(mainframe, textvariable=password, width=12, bd=2, font=("arial", 30), show="*")
    entry_password.place(x=400, y=150)

    # button
    def reset():
        entry_username.delete(0, END)
        entry_password.delete(0, END)

    Button(mainframe, text="Login", height="3", width="23", bg="#ed3833", fg="white", bd=0, font=("arial", 10),command=login).place(x=100, y=250)
    Button(mainframe, text="Reset", height="3", width="23", bg="#1089ff", fg="white", bd=0, command=reset,font=("arial", 10)).place(x=300, y=250)
    Button(mainframe, text="Exit", height="3", width="23", bg="#00bd56", fg="white", bd=0, command=screen.destroy,font=("arial", 10)).place(x=500, y=250)
    screen.mainloop()


main_screen()
