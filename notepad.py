from tkinter import *
from tkinter import filedialog

window=Tk()
window.title('Notepad')
window.geometry('500x500')

def open_file():
	o=filedialog.askopenfile(mode='r',filetype=[('all','*.*')])
	if o is not None:
		openedfile=o.read()
    
	entry.delete(1.0,END)
	entry.insert(INSERT,openedfile)

def clear():
	entry.delete(1.0,END)

def save_file():
	s=filedialog.asksaveasfile(mode='w')
	if s is None:
		return
	txt=str(entry.get(1.0,END))
	s.write(txt)
	s.close()

menubar=Menu(window)
window.config(menu=menubar)

menu1=Menu(menubar)
menubar.add_cascade(label='Open',command=open_file)
menubar.add_cascade(label='Save',command=save_file)
menubar.add_cascade(label='clear',command=clear)

entry=Text(window,height=30,width=60,wrap=WORD)
entry.place(x=5,y=5)

window.mainloop()
