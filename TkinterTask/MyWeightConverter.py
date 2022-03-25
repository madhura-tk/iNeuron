# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.7
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# +
from tkinter import *
from tkinter import  StringVar, ttk
from tkinter import messagebox as mb


class MyWeightConverter:

    def __init__(self, root):
        self.root = root
        self.root.title('Weight Converter')
        self.root.geometry("450x400+100+200")
        l = Label(self.root, text='Weight Converter App', font=("Arial", 20, "italic"), justify=CENTER)
        l.place(x=80, y=20)

        self.factors = {'kg': 1000, 'hg': 100, 'dg': 10, 'g': 1, 'deg': 0.1, 'cg': 0.01, 'mg': 0.001}
        self.ids = {"Kilogram": 'kg', "Hectagram": 'hg', "Decagram": 'dg', "Decigram": 'deg',"Gram": 'g', "Centigram": 'cg', "Milligram": 'mg'}
        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.pack(fill=BOTH, expand=1)

        self.in_amt = StringVar()
        self.in_amt.set('0.0')
        self.out_amt = StringVar()

        self.in_unit = StringVar()
        self.out_unit = StringVar()
        self.in_unit.set('Select Unit')
        self.out_unit.set('Select Unit')

        self.in_field = ttk.Entry(mainframe, width=20, textvariable=self.in_amt)
        self.in_field.grid(row=1, column=2, sticky="W")
        in_select = OptionMenu(mainframe, self.in_unit, "Kilogram", "Hectagram", "Decagram", "Gram", "Decigram",
                               "Centigram", "Milligram").grid(column=3, row=1, sticky=W)

        ttk.Entry(mainframe, textvariable=self.out_amt, state="readonly").grid(column=2, row=2, sticky="W")
        self.in_select = OptionMenu(mainframe, self.out_unit, "Kilogram", "Hectagram", "Decagram", "Gram", "Decigram",
                                    "Centigram", "Milligram").grid(column=3, row=2, sticky=W)

        calc_button = ttk.Button(mainframe, text="Calculate", command=self.callback).grid(column=2, row=3, sticky=E)

        root.mainloop()

    def convert(self, amt, frm, to):
        if frm != 'g':
            amt = amt * self.factors[frm]
            return amt / self.factors[to]
        else:
            return amt / self.factors[to]

    def callback(self):
        try:
            amt = float(self.in_field.get())
        except ValueError:
            mb.showerror(title='Error!',
                         message=f'Please Enter a Correct Value')
            return None
        if self.in_unit.get() == 'Select Unit' or self.out_unit.get() == 'Select Unit':
            mb.showinfo("Info",
                        message=f'Please choose the Input/Output Unit')
            return None
        else:
            frm = self.ids[self.in_unit.get()]
            to = self.ids[self.out_unit.get()]
            self.out_amt.set(self.convert(amt, frm, to))



# -


