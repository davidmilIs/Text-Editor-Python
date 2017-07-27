from tkinter import *
from tkinter.filedialog import *

filename = "Untilted"

def newFile():
    global filename
    filename ="Untilted"
    text.delete("1.0",END)
    #1,0 Line number, Column Number

def saveFile():
    global filename
    t=text.get("1.0",END)
    f=open(filename,'w')
    f.write(t)
    f.close()

def saveAs():
    f = asksaveasfile(defaultextension='.txt')
    t= text.get("1.0",END)
    print(t)
    try:
        f.write(t.rstrip())
        f.close
    except:
        print("Error")

def openFile():
    f=askopenfile(parent=root,title='Select a File')
    t=f.read()
    text.delete("1.0",END)
    text.insert("1.0",t)

root = Tk()
root.title("Python Text Editor")
root.minsize(width=640,height=400)
root.maxsize(width=640,height=400)


text = Text(root, width=640,height=400)
text.configure(background="bisque")
text.pack()


menubar =Menu(root)
filemenu =Menu(menubar)
filemenu.add_command(label="New",command=newFile)
filemenu.add_command(label="Open",command=openFile)
filemenu.add_command(label="Save",command=saveFile)
filemenu.add_command(label="Save As",command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="Quit",command=root.quit)
menubar.add_cascade(label="File",menu=filemenu)

root.config(menu=menubar)
root.mainloop()
