

from tkinter import *
class MyCalculator:

    def click_button(self, numbers):
        global operator
        global var

        self.operator = self.operator + str(numbers)
        self.var.set(self.operator)

    def clear(self):
        self.entry.delete(0, END)
        self.operator = ""
        self.var.set("0")

    def evaluate(self):
        try:
            self.answer = eval(self.entry.get())
            self.var.set(self.answer)
            self.operator = str(self.answer)
        except:
            self.operator = ""
            self.var.set("ERR")
            
    def on_closing(self):
        self.root. destroy()

    def __init__(self, root):
        self.root=root
        img = PhotoImage(file="img/calc.png")
        self.root.title("My Calculator")
        self.root.iconphoto(False, img)
        self.root.geometry("400x300")
        self.operator = ""
        self.var = StringVar()
        self.var.set("0")

        self.entry = Entry(self.root, textvariable=self.var, bg='white', width=45, bd=20, justify='right',
                           font=('arial', 10, 'bold'))
        self.entry.pack()
        self.t = Text(self.entry, height=40)
        self.entry.config(state='readonly')

        label_key = Label(self.root, height=15, width=30, bd=10, bg='gray50')
        label_key.pack(side=LEFT, fill=BOTH, expand=True)

        label_fkey = Label(self.root, height=15, width=20, bd=10, bg='gray50')
        label_fkey.pack(side=LEFT, fill=BOTH, expand=True)

        label_7 = Label(label_key, bg='black')
        label_7.grid(row=0, column=0)
        button_7 = Button(label_7, text='7', font=('Arial', '16'), width=4, command=lambda: self.click_button(7),
                          bg='black', fg='white')
        button_7.pack()

        label_8 = Label(label_key, bg='black')
        label_8.grid(row=0, column=1, padx=5)
        button_8 = Button(label_8, text='8', font=('Arial', '16'), width=4, command=lambda: self.click_button(8),
                          bg='black', fg='white')
        button_8.pack()

        label_9 = Label(label_key, bg='black')
        label_9.grid(row=0, column=2, padx=0)
        button_9 = Button(label_9, text='9', font=('Arial', '16'), width=4, command=lambda: self.click_button(9),
                          bg='black', fg='white')
        button_9.pack()

        label_4 = Label(label_key, bg='black')
        label_4.grid(row=1, column=0, padx=5, pady=10)
        button_4 = Button(label_4, text='4', font=('Arial', '16'), width=4, command=lambda: self.click_button(4),
                          bg='black', fg='white')
        button_4.pack()

        label_5 = Label(label_key, bg='black')
        label_5.grid(row=1, column=1, padx=5, pady=10)
        button_5 = Button(label_5, text='5', font=('Arial', '16'), width=4, command=lambda: self.click_button(5),
                          bg='black', fg='white')
        button_5.pack()

        label_6 = Label(label_key, bg='black')
        label_6.grid(row=1, column=2, padx=0, pady=10)
        button_6 = Button(label_6, text='6', font=('Arial', '16'), width=4, command=lambda: self.click_button(6),
                          bg='black', fg='white')
        button_6.pack()

        label_1 = Label(label_key, bg='black')
        label_1.grid(row=2, column=0, padx=5)
        button_1 = Button(label_1, text='1', font=('Arial', '16'), width=4, command=lambda: self.click_button(1),
                          bg='black', fg='white')
        button_1.pack()

        label_2 = Label(label_key, bg='black')
        label_2.grid(row=2, column=1, padx=5)
        button_2 = Button(label_2, text='2', font=('Arial', '16'), width=4, command=lambda: self.click_button(2),
                          bg='black', fg='white')
        button_2.pack()

        label_3 = Label(label_key, bg='black')
        label_3.grid(row=2, column=2, padx=0)
        button_3 = Button(label_3, text='3', font=('Arial', '16'), width=4, command=lambda: self.click_button(3),
                          bg='black', fg='white')
        button_3.pack()

        label_0 = Label(label_key, bg='black')
        label_0.grid(row=3, column=0, padx=5, pady=10)
        button_0 = Button(label_0, text='0', font=('Arial', '16'), width=4, command=lambda: self.click_button(0),
                          bg='black', fg='white')
        button_0.pack()

        label_deci = Label(label_key, bg='black')
        label_deci.grid(row=3, column=1, padx=5, pady=10)
        button_deci = Button(label_deci, text='.', font=('Arial', '16'), width=4,
                             command=lambda: self.click_button('.'), bg='black', fg='white')
        button_deci.pack()

        label_equal = Label(label_key, bg='black')
        label_equal.grid(row=3, column=2, padx=5, pady=0)
        button_equal = Button(label_equal, text='=', font=('Arial', '16'), width=4, command=self.evaluate,
                              bg='lightgrey', fg='black')
        button_equal.pack()

        label_C = Label(label_fkey, bg='black')
        label_C.grid(row=1, column=0, columnspan=2)
        button_C = Button(label_C, text='C', font=('Arial', '16'), height=1, width=8, command=self.clear, bg='red',
                          fg='white')
        button_C.pack(side=LEFT)

        label_sub = Label(label_fkey, bg='black')
        label_sub.grid(row=2, column=0, sticky=W, pady=10)
        button_sub = Button(label_sub, text='-', font=('Arial', '16'), height=1, width=3,
                            command=lambda: self.click_button('-'), bg='lightgrey', fg='black')
        button_sub.pack(side=LEFT)

        label_mul = Label(label_fkey, bg='black')
        label_mul.grid(row=2, column=1, sticky=E)
        button_mul = Button(label_mul, text='x', font=('Arial', '16'), height=1, width=3,
                            command=lambda: self.click_button('*'), bg='lightgrey', fg='black')
        button_mul.pack()

        label_div = Label(label_fkey, bg='black')
        label_div.grid(row=3, column=0, sticky=W)
        button_div = Button(label_div, text='/', font=('Arial', '16'), height=1, width=3,
                            command=lambda: self.click_button('/'), bg='lightgrey', fg='black')
        button_div.pack()

        label_add = Label(label_fkey, bg='black')
        label_add.grid(row=3, column=1, sticky=E)
        button_add = Button(label_add, text='+', font=('Arial', '16'), height=1, width=3,
                            command=lambda: self.click_button('+'), bg='lightgrey', fg='black')
        button_add.pack()

        label_mod = Label(label_fkey, bg='black')
        label_mod.grid(row=4, column=0, sticky=W, pady=10)
        button_mode = Button(label_mod, text='%', font=('Arial', '16'), height=1, width=3,
                             command=lambda: self.click_button('%'), bg='lightgrey', fg='black')
        button_mode.pack()

        label_floor = Label(label_fkey, bg='black')
        label_floor.grid(row=4, column=1, sticky=E, pady=10)
        button_floor = Button(label_floor, text='//', font=('Arial', '16'), height=1, width=3,
                              command=lambda: self.click_button('//'), bg='lightgrey', fg='black')
        button_floor.pack()
        
        self.root. protocol("WM_DELETE_WINDOW", self.on_closing)

        self.root.mainloop()






