#importing required packages and libraries

from tkinter import *
from datetime import datetime
from tkinter import messagebox
from tkinter import filedialog,simpledialog
from tkinter.scrolledtext import ScrolledText

class MyNotepad:

    # defining functions for commands
    def cmdNew(self):  # file menu New option
        global fileName
        if len(self.notepad.get('1.0', END + '-1c')) > 0:
            if messagebox.askyesno("Notepad", "Do you want to save changes?"):
                self.cmdSave()
            else:
                self.notepad.delete(0.0, END)
        self.root.title("Notepad")

    def cmdOpen(self):  # file menu Open option
        fd = filedialog.askopenfile(parent=self.root, mode='r')
        t = fd.read()  # t is the text read through filedialog
        self.notepad.delete(0.0, END)
        self.notepad.insert(0.0, t)

    def cmdSave(self):  # file menu Save option
        fd = filedialog.asksaveasfile(defaultextension='.txt', mode='w',filetypes=[("All Files","*.*"),
                                      ("Text Documents","*.txt")])
        if fd != None:
            data = self.notepad.get('1.0', END)
        try:
            fd.write(data)
        except:
            messagebox.showerror(title="Error", message="Not able to save file!")

    def cmdSaveAs(self):  # file menu Save As option
        fd = filedialog.asksaveasfile(mode='w', defaultextension='.txt',filetypes=[("All Files","*.*"),
                                      ("Text Documents","*.txt")])
        t = self.notepad.get(0.0, END)  # t stands for the text gotten from notepad
        try:
            fd.write(t.rstrip())
        except:
            messagebox.showerror(title="Error", message="Not able to save file!")

    def cmdExit(self):  # file menu Exit option
        if messagebox.askyesno("Notepad", "Are you sure you want to exit?"):
            self.root.destroy()

    def cmdCut(self):  # edit menu Cut option
        self.notepad.event_generate("<<Cut>>")

    def cmdCopy(self):  # edit menu Copy option
        self.notepad.event_generate("<<Copy>>")

    def cmdPaste(self):  # edit menu Paste option
        self.notepad.event_generate("<<Paste>>")

    def cmdClear(self):  # edit menu Clear option
        self.notepad.event_generate("<<Clear>>")

    def cmdFind(self):  # edit menu Find option
        self.notepad.tag_remove("Found", '1.0', END)
        find = simpledialog.askstring("Find", "Find what:")
        if find:
            idx = '1.0'  # idx stands for index
        while 1:
            idx = self.notepad.search(find, idx, nocase=1, stopindex=END)
            if not idx:
                break
            lastidx = '%s+%dc' % (idx, len(find))
            self.notepad.tag_add('Found', idx, lastidx)
            idx = lastidx
        self.notepad.tag_config('Found', foreground='white', background='blue')
        self.notepad.bind("<1>", self.click)

    def click(self, event):  # handling click event
        self.notepad.tag_config('Found', background='white', foreground='black')

    def cmdSelectAll(self):  # edit menu Select All option
        self.notepad.event_generate("<<SelectAll>>")

    def cmdTimeDate(self):  # edit menu Time/Date option
        now = datetime.now()
        # dd/mm/YY H:M:S
        dtString = now.strftime("%d/%m/%Y %H:%M:%S")
        label = messagebox.showinfo("Time/Date", dtString)

    def cmdAbout(self):  # help menu About option
        label = messagebox.showinfo("notepad","Notepad in Tkinter")

    def __init__(self,root):
        #the root widget
        self.root = root
        self.root.title('MyNotepad')
        self.root.resizable(0, 0)
        #creating scrollable notepad window
        self.notepad = ScrolledText(self.root, width = 90, height = 40)
        self.fileName = ' '
            #notepad menu items
        self.notepadMenu = Menu(self.root)
        self.root.configure(menu=self.notepadMenu)

        #file menu
        self.fileMenu = Menu(self.notepadMenu, tearoff = False)
        self.notepadMenu.add_cascade(label='File', menu = self.fileMenu)

        #adding options in file menu
        self.fileMenu.add_command(label='New', command = self.cmdNew)
        self.fileMenu.add_command(label='Open...', command = self.cmdOpen)
        self.fileMenu.add_command(label='Save', command = self.cmdSave)
        self.fileMenu.add_command(label='Save As...', command = self.cmdSaveAs)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label='Exit', command = self.cmdExit)

        #edit menu
        self.editMenu = Menu(self.notepadMenu, tearoff = False)
        self.notepadMenu.add_cascade(label='Edit', menu = self.editMenu)

        #adding options in edit menu
        self.editMenu.add_command(label='Cut', command = self.cmdCut)
        self.editMenu.add_command(label='Copy', command = self.cmdCopy)
        self.editMenu.add_command(label='Paste', command = self.cmdPaste)
        self.editMenu.add_command(label='Delete', command = self.cmdClear)
        self.editMenu.add_separator()
        self.editMenu.add_command(label='Find...', command = self.cmdFind)
        self.editMenu.add_separator()
        self.editMenu.add_command(label='Select All', command = self.cmdSelectAll)
        self.editMenu.add_command(label='Time/Date', command = self.cmdTimeDate)

        #help menu
        self.helpMenu = Menu(self.notepadMenu, tearoff = False)
        self.notepadMenu.add_cascade(label='Help', menu = self.helpMenu)

        #adding options in help menu
        self.helpMenu.add_command(label='About Notepad', command = self.cmdAbout)
        self.notepad.pack()
        self.root.mainloop()

