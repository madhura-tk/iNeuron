
import tkinter
from tkinter import *
import tkinter.filedialog as fd
import tkinter.messagebox as mb
from tkinter import ttk
import os
import shutil

class MyFileExplorer:

    def open_file(self):
        try:
            file = fd.askopenfilename(title='Choose a file of any type', filetypes=[("All files", "*.*")])
            os.startfile(os.path.abspath(file))
        except:
            mb.showerror(title='Error!',
                         message='We were unable to open your file to the desired location. Please try again')

    def copy_file(self):
        file_to_copy = fd.askopenfilename(title='Choose a file to copy', filetypes=[("All files", "*.*")])
        dir_to_copy_to = fd.askdirectory(title="In which folder to copy to?")

        try:
            shutil.copy(file_to_copy, dir_to_copy_to)
            mb.showinfo(title='File copied!', message='Your desired file has been copied to your desired location')
        except:
            mb.showerror(title='Error!',
                         message='We were unable to copy your file to the desired location. Please try again')
    
    '''def on_closing(self):
        if mb.askokcancel("Quit", "Do you want to quit?"):
            self.root. destroy()'''
        
    def delete_file(self):
        file = fd.askopenfilename(title='Choose a file to delete', filetypes=[("All files", "*.*")])
        try:
            os.remove(os.path.abspath(file))
            mb.showinfo(title='File deleted', message='Your desired file has been deleted')
        except:
            mb.showerror(title='Error!',
                         message='We were unable to delete your file to the desired location. Please try again')

    def list_files_in_folder(self):
        self.resultArea.grid(self.resultArea._grid_info)
        self.sb.grid(self.sb._grid_info)
        i = 0
        folder = fd.askdirectory(title='Select the folder whose files you want to list')
        try:
            files = os.listdir(os.path.abspath(folder))
            self.resultArea.configure(state='normal')
            self.resultArea.delete('1.0', END)
            while i < len(files):
                self.resultArea.insert(END, files[i] + '\n')
                i += 1
            self.resultArea.configure(state='disable')
        except Exception as e:
            mb.showerror(title='Error!',
                         message=f'{e}  We were unable to list your files to the desired location. Please try again')

    def __init__(self, root):
        title = 'My File Explorer'
        background = 'white'

        button_font = ("Times New Roman", 13)
        button_background = 'thistle1'
        self.root = root

        # Initializing the window
        self.root.title(title)
        self.root.geometry('650x600')
        self.root.resizable(True,True)
        self.root.config(bg=background)

        # Creating and placing the components in the window
        label = Label(self.root, text=title, font=("Comic Sans MS", 15), bg=background, wraplength=250)
        label.grid(row=0, column=0, padx=15)

        button_open = Button(self.root, text='Open a file', width=20, font=button_font, bg=button_background,
                             command=self.open_file)
        button_open.grid(row=1, column=0, padx=15)

        button_copy = Button(self.root, text='Copy a file', width=20, font=button_font, bg=button_background,
                             command=self.copy_file)
        button_copy.grid(row=2, column=0, padx=15)

        button_delete = Button(self.root, text='Delete a file', width=20, font=button_font, bg=button_background,
                               command=self.delete_file)
        button_delete.grid(row=3, column=0, padx=15)

        button_listfiles = Button(self.root, text='List all files in a folder', width=20, font=button_font,
                                  bg=button_background, command=self.list_files_in_folder)
        button_listfiles.grid(row=4, column=0, padx=15)

        self.lf=Frame(self.root)
        self.lf.grid(row=5,column=1)
        self.resultArea = Text(self.lf, width=30,background="white",borderwidth=40,border=2,)
        self.resultArea.grid(row=0, column=0)

        self.sb = Scrollbar(self.lf,orient=VERTICAL)
        self.sb.grid(row=0, column=1, sticky=NS)

        self.resultArea.config(yscrollcommand=self.sb.set)
        self.sb.config(command=self.resultArea.yview)
        self.resultArea.configure(state='disable')
        self.resultArea._grid_info=self.resultArea.grid_info()
        self.sb._grid_info=self.sb.grid_info()
        self.sb.grid_remove()
        self.resultArea.grid_remove()

        #button_exit=Button(self.root,text = "Exit",command = lambda:root.destroy(),width=20, font=button_font, bg=button_background)
        #button_exit.grid(row=10, column=2, padx=35)

        # Finalizing the window
        self.root.update()
        #self.root. protocol("WM_DELETE_WINDOW", self.on_closing)

        self.root.mainloop()





