from tkinter import *
import tkinter.filedialog

filename = None

def newFile():
    global filename
    filename ="Untilted"
    text.delete(0,0,END)
    #0,0 Line number, Column Number

def saveFile():
    global filename
    t=text.get(0,0,END)
    f=open(filename,'w')
    f.write(t)
    f.close()

def saveAs():
    f=asksaveasfile(mode='w',deffaultextension='.txt')
    t= text.get(0,0,END)
    try:
        f.write(t.rstrip())
    except:
        showerror(title="Error !",message="Unable to save file..")

def openFile():
    f=askopenfile(mode='r')
    t=f.read()
    text.delete(0,0,END)
    text.insert(0,0,t)

root = Tk()
root.title("Python Text Editor")
root.minsize(width=640,height=400)
root.maxsize(width=640,height=400)

text = Text(root, width=640,height=400)
text.pack()

menubar =Menu(root)
filemenu =Menu(menubar)
filemenu.add_command(label="New",command=newFile)

filemenu.add_command(label="New",command=newFile)
filemenu.add_command(label="Open",command=openFile)
filemenu.add_command(label="Save",command=saveFile)
filemenu.add_command(label="Save As",command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="Quit",command=root.quit)
menubar.add_cascade(label="File",menu=filemenu)

root.config(menu=menubar)
root.mainloop()
