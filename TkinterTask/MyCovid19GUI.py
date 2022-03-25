from tkinter import *
from pandastable import Table, TableModel
import pandas as pd

class MyCovid19GUI(Frame):
    """Basic test frame for the table"""
    def __init__(self,parent=None):
        self.parent = parent
        Frame.__init__(self)
        #self.main = self.master
        self.parent.geometry('600x400+200+100')
        self.parent.title('Table app')
        f = Frame(self.parent)
        f.pack(fill=BOTH,expand=1)
        
        url = "https://data.covid19india.org/v4/min/data.min.json"
        data = pd.read_json(url)
        df1 = pd.DataFrame(data)
        df2 = df1.T
        df3 = df2["total"]
        df4 = pd.DataFrame(pd.json_normalize(df2['total']))
        df5 = df4.T
        df5.columns = df1.columns
        df5.insert(0, "States", value=df5.index)
        
        df5.fillna(0)
        
        self.table = pt = Table(f, dataframe=df5,
        showtoolbar=True, showstatusbar=True)
        pt.show()
        return


# -




