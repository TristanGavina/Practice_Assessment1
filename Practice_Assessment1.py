"""Practice Assessment"""

from tkinter import *

def quit():
    main_window.destroy()
#printing information
def print_names():
    global details, total_entries, info
    info=0
    Label(main_window,text='Group Leader:').grid(column=0,row=8)
    Label(main_window,text='Number of Campers:').grid(column=1,row=8)
    Label(main_window,text='Location:').grid(column=2,row=8)
    Label(main_window,text='Weather:').grid(column=3,row=8)
    Label(main_window,text='Command to move:').grid(column=4,row=8)
    while info<total_entries:
        Label(main_window, text=info).grid(column=0,row=info+9)
        Label(main_window, text=(details[info][0])).grid(column=0,row=info+9)
        Label(main_window, text=(details[info][1])).grid(column=1,row=info+9)
        Label(main_window, text=(details[info][2])).grid(column=2,row=info+9)
        Label(main_window, text=(details[info][3])).grid(column=3,row=info+9)
        Label(main_window, text=(details[info][4])).grid(column=4,row=info+9)
        info += 1
#appending info
def append_name():
    global details,entry_gl,entry_nc,entry_l,entry_w,entry_cm,total_entries
    if len(entry_gl.get()) !=0:
        details.append([entry_gl.get(),entry_nc.get(),entry_l.get(),entry_w.get(),entry_cm.get()])
        entry_gl.delete(0,'end')
        entry_nc.delete(0,'end')
        entry_l.delete(0,'end')
        entry_w.delete(0,'end')
        entry_cm.delete(0,'end')
        total_entries += 1
#for deleting a row
def delete_row ():
    global details, delete_item, total_entries, info
    del details[int(delete_item.get())]
    total_entries = total_entries - 1
    delete_item.delete(0,'end')
    Label(main_window, text="       ").grid(column=0,row=info+8) 
    Label(main_window, text="       ").grid(column=1,row=info+8)
    Label(main_window, text="       ").grid(column=2,row=info+8)
    Label(main_window, text="       ").grid(column=3,row=info+8)
    Label(main_window, text="       ").grid(column=4,row=info+8)
    print_names()
#making the buttons
def buttons():
    global details,entry_gl,entry_nc,entry_l,entry_w,entry_cm,total_entries,delete_item
    Button(main_window, text="Quit", command=quit).grid(column=1, row=0)
    Button(main_window, text="Append Details", command=append_name).grid(column=0, row=1)
    Button(main_window, text="Print Details", command=print_names).grid (column=1, row=1)
    Label(main_window, text="Group Leader:").grid (column=0, row=2)
    entry_gl = Entry(main_window)
    entry_gl.grid(column=1, row=2)
    Label(main_window, text="Number of Campers:").grid(column=0, row=3)
    entry_nc =Entry(main_window)
    entry_nc.grid(column=1, row=3)
    Label(main_window, text="Location:").grid(column=0, row=4)
    entry_l = Entry(main_window)
    entry_l.grid(column=1, row=4)
    Label(main_window, text="Weather:").grid(column=0, row=5)
    entry_w = Entry(main_window)
    entry_w.grid(column=1, row=5)
    Label(main_window, text="Command to move:").grid(column=0, row=6)
    entry_cm = Entry(main_window)
    entry_cm.grid(column=1, row=6)
    Label(main_window, text="Delete Row #:") .grid(column=0,row=7)
    delete_item = Entry(main_window)
    delete_item .grid(column=1,row=7)
    Button(main_window, text="Delete",command=delete_row) .grid(column=2,row=7)
def main():
    global main_window
    global details,entry_gl,entry_nc,entry_l,entry_w,enry_cm,total_entries
    details = []
    total_entries = 0
    main_window =Tk()
    buttons ()
    main_window.mainloop()
main()
