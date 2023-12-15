import tkinter
from tkinter import ttk
from tkinter import messagebox
form=tkinter.Tk()
form.geometry("700x500")

fnt =("tahoma",20)
btns=ttk.Style()
btns.configure("TButton",font =fnt,buckgrounf ="#ffffff")

lbl = ttk.Label(form,font =fnt)
txt = ttk.Entry(form,font = fnt)
def sayhello():
    messagebox.showinfo("welcome","hello " +txt.get())

btn =ttk.Button(form,text="click here",style ="TButton",command =sayhello)

lbl.pack()
txt.pack()
btn.pack()
 
