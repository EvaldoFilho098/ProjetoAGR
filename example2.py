from tkinter import *
from tkinter import ttk
import tkinter as tk

tablename = 'list_all'
df = Expenses_SQL_Create_Table.read_from_table_2(tablename)

df = df.astype(int)
for i in range(1,len(df.columns)+1):
    df[df.columns[i-1]] = df[df.columns[i-1]].apply(lambda x : "{:,}".format(x))

df.reset_index(inplace=True)
rows = df.values.tolist()

root = Tk()

def treeframe():

    frm = Frame(root)
    frm.pack(padx=0, pady=10, anchor='nw')

    frm.pack(padx=0,pady=10)

    tv = ttk.Treeview(frm,columns=(1,2,3,4,5,6,7,8,9,10,11,12),show = 'headings',height='50')
    tv.pack()

    tv.column("#0", minwidth=100, width=100)
    tv.column(1, minwidth=0, width=150)

    for i in range(2,13):
        tv.column(i, minwidth=0, width=70)


    tv.heading(1,text='Date')
    tv.heading(2,text='Expense')

    tv.column("#0", minwidth=0, width=100, stretch=NO)

    for i in rows:
        tv.insert('','end',values=i)


def treeframe1():


    root.minsize(width=600, height=700)
    #root.resizable(width=0, height=0)

    tree = ttk.Treeview(root, selectmode='browse',height='10')
    tree.place(x=330, y=45)

    #Vertical scroll bar
    vsb = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
    vsb.place(x=320, y=45, height=200 + 180)
    tree.configure(yscrollcommand=vsb.set)

    #Horizontal scroll bar
    hsb = ttk.Scrollbar(root, orient="horizontal", command=tree.xview)
    hsb.place(x=320, y=445)
    tree.configure(xscrollcommand=hsb.set)

    tree["columns"] = list(range(1, len(df.columns)+1))
    tree['show'] = 'headings'
    tree['height'] = '20'

    colnames = df.columns

    tree.column(1, width=90,anchor='c')
    tree.heading(1, text=colnames[0])


    for i in range(2,len(df.columns)+1):
        tree.column(i, width=100,anchor='c')
        tree.heading(i, text=colnames[i-1])

    for i in rows:
        tree.insert('','end',values=i)


    def delete_command():
        tree["columns"] = ()
        #tree.delete(*tree.get_children())

    b2 = Button(root, text="delete all", width=12, command=delete_command)
    # b1.grid(row=10,column=8)
    b2.place(x=130, y=45)


treeframe1()





root.title('New Data')
root.geometry('650x500')
#root.resizable(False,False)
root.mainloop()