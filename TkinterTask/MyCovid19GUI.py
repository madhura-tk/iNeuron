from tkinter import *


'''Introduction
The pandastable library provides a table widget for Tkinter with plotting and data manipulation functionality.
It uses the pandas DataFrame class to store table data. Pandas is an open source Python library providing high-performance data structures and data analysis tools. 
Tkinter is the standard GUI toolkit for python. It is intended for the following uses:

for python/tkinter GUI developers who want to include a table in their application that can store and process large amounts of data
for non-programmers who are not familiar with Python or the pandas API and want to use the included DataExplore application to manipulate/view their data
it may also be useful for data analysts and programmers who want to get an initial interactive look at their tabular data without coding
The DataExplore application
Installing the package creates a command dataexplore in your path. Just run this to open the program. This is a standalone application 
for data manipulation and plotting meant for education and basic data analysis.
See the home page for this application at http://dmnfarrell.github.io/pandastable/

Links
http://openresearchsoftware.metajnl.com/articles/10.5334/jors.94/

http://dmnfarrell.github.io/pandastable/

https://youtu.be/Ss0QIFywt74

!pip install pandastable
'''

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
        
        
        self.table = pt = Table(f, dataframe=df5,
        showtoolbar=True, showstatusbar=True)
        pt.show()
        return






