from tkinter import *
from datetime import date
import tkinter.messagebox as mb
class MyAgeCalculator:
    # defining a function to calcutate age
    def age(self):
        global today
        self.new.grid_forget()
        try:
            b_date = int(self.entry_date.get())
            b_month = int(self.entry_month.get())
            b_year = int(self.entry_year.get())
            c_date = int(self.list_today[2])
            c_month = int(self.list_today[1])
            c_year = int(self.list_today[0])
            month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            if (b_date > c_date):
                c_month = c_month - 1
                c_date = c_date + month[b_month - 1]
            if (b_month > c_month):
                c_year = c_year - 1
                c_month = c_month + 12
            resultd = str(c_date - b_date)
            resultm = str(c_month - b_month)
            resulty = str(c_year - b_year)
            self.new = Label(self.root,
                             text="YOUR AGE \n" + resulty + " YEARS " + resultm + " MONTHS " + resultd + " DAYS ",
                             fg="#FFFFFF", bg="#3498DB", borderwidth=6, padx=10)
            self.new.config(font=("Arial Rounded MT Bold", 10))
            self.new.grid(row=5, column=0, columnspan=3)
        except ValueError :
            mb.showerror("Error","Please Enter a Correct Value")
        except Exception as e :
            mb.showerror("Error",f"{e} Error occured")


    # defining a function to clear the previous entries
    def clean(self):

        self.new.grid_forget()
        self.entry_date.delete(0, END)
        self.entry_month.delete(0, END)
        self.entry_year.delete(0, END)

    def callback(self,input):

        if input.isdigit():
            print(input)
            return True

        elif input == "":
            print(input)
            return True

        else:
            print(input)
            return False

    def __init__(self,root):
            self.root=root
            self.root.title("AGE-CALCULATOR")
            self.root.configure(bg="#D5C6FF")
            self.root.geometry("500x300")
            self.new=Label(self.root,bg="#000000")
            self.new.grid(row=5,column=0,columnspan=3)

            today=str(date.today())
            self.list_today=today.split("-")
            #creating widgets such as labels,entry boxes and buttons and fixing its position onto window
            self.title_label=Label(self.root,text="AGE CALCULATOR",borderwidth=35,fg="#36454F",bg="#A7C7E7")
            self.title_label.config(font=("Broadway",29))
            self.title_label.grid(row=0,column=0,columnspan=3)
            self.label_date=Label(self.root,text="BIRTH DATE : ",borderwidth=4,fg="#088F8F",bg="#D5C6FF")
            self.label_date.config(font=("Arial Rounded MT Bold",15))
            self.label_date.grid(row=1,column=0)
            self.label_month=Label(self.root,text="BIRTH MONTH : ",borderwidth=5,fg="#088F8F",bg="#D5C6FF")
            self.label_month.config(font=("Arial Rounded MT Bold",15))
            self.label_month.grid(row=2,column=0)
            self.label_year=Label(self.root,text="BIRTH YEAR : ",borderwidth=9,fg="#088F8F",bg="#D5C6FF")
            self.label_year.config(font=("Arial Rounded MT Bold",15))
            self.label_year.grid(row=3,column=0)

            self.entry_date=Entry(self.root,width=20,borderwidth=3)

            self.entry_month=Entry(self.root,width=20,borderwidth=3)

            self.entry_year=Entry(self.root,width=20,borderwidth=3)

            self.entry_date.grid(row=1,column=2)
            self.entry_month.grid(row=2,column=2)
            self.entry_year.grid(row=3,column=2)

            #calling age function in button widget
            submit=Button(self.root,text="GET AGE!!",width=10,anchor=CENTER,command=lambda:self.age(),bg="#008080",fg="#FFFFFF",borderwidth=5)
            submit.grid(row=4,column=0)

            #calling clean function in button widget
            clear=Button(self.root,text="CLEAR",width=10,command=lambda:self.clean(),bg="#008080",fg="#FFFFFF",borderwidth=5)
            clear.grid(row=4,column=2)
            self.new.grid_forget()
            root.mainloop()

