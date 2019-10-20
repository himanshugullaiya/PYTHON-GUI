########## Note ##########
""" We can call and use a library in two ways :-
   1) import tkinter as tk
   2) from tkinter import * - import all functions

1) whenever we refer any function of this library we will use
a) tk.label()
b) tk.Tk()

2) we will use the function name directly without referrring it to that class
a) label()
b) Tk()
"""

from tkinter import *


#Using Text in labels
root = Tk()
w1 = Label(root, text = "Hello world")
w1.pack()
root.mainloop()


#Using Image in labels
root = Tk()
logo = PhotoImage(file = "python_logo.gif")
explanation = """At present, only GIF and PPM/PGM
formats are supported, but an interface
exists to allow additional image file
formats to be added easily."""

w2_1 = Label(root, image = logo)
w2_1.pack(side = "right")
w2_2 = Label(root, justify = LEFT, padx = 5, text = explanation, fg = "red", font = ("Times", 20 , "italic"), bg = '#%02x%02x%02x' % (189,250,250,))
w2_2.pack(side = "left")
root.mainloop()

# draws text on top of image
'''
w2_2 = Label(root, compound = CENTER, justify = LEFT, padx = 5, text = explanation, image = logo)
w2_2.pack(side = "left")
root.mainloop()
'''

#Dynamic content in  a label
counter = 0
def counter_label(label):
  def count():
    global counter
    counter += 1
    label.config(text=str(counter))
    label.after(1000, count)
  count()

root = Tk()
root.title("Counting Seconds")
label = Label(root, fg="green", bg = "black")
label.pack()
counter_label(label)
button = Button(root, text='Stop', width=25, command=root.destroy)
button.pack()
root.mainloop()

#efbot
#Wrappng code in one or more classes
#hello world

class App:

    def __init__(self, master):
          
        frame = Frame(master)
        frame.pack()
        self.button = Button(
            frame, text="QUIT", fg="red", bg="black",command=frame.quit)
        self.button.grid(row = 0, column = 0)
        
        self.hi_there = Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.grid(row= 0, column = 1)

    def say_hi(self):
        print("hi there, everyone!")

root = Tk()
app = App(root)
root.mainloop()
root.destroy()

# Messages

root = Tk()
txt = "Hello, i am the best coder in my class"
msg = Message(root, text = txt)
msg.config(bg = "lightgreen", font = "Times 20 italic")
msg.pack()

bttn = Button(root, text = "QUIT", fg = "red", width = "25",command = root.quit)
bttn.pack(side = BOTTOM)
root.mainloop()
root.destroy()

# Radiobutton

root = Tk()
v = IntVar()
v.set(1)
languages = [("Python",1),("C",2),("C++",3),("C#",4),("JAVA",5),("KOTLIN",6)]
            
def ShowChoice():
      print(v.get())

txt = """Choose any Programming 
            Langauage: """

Label(root, text = txt, font = "TIMES 16 bold", justify = 'left', padx = 20).pack()

for language,val in languages:
      Radiobutton(root, text = language, justify = LEFT, variable = v, padx = 20,command = ShowChoice, value = val).pack(anchor = W)

root.mainloop()
root.destroy()

##########################################
# Using grid 

root = Tk()
for r in range(3):
      for c in range(3):
            Label(root, text='R%s/C%s'%(r,c), borderwidth=20).grid(row=r,column=c)
root.mainloop(  )
root.destroy()

##############################################
#using checkboxes
root = Tk()
def var_states():
      print("Male : %d, Female: %d" % (var1.get(), var2.get()))

Label(root, text = "Your Sex: ", padx = 15).grid(row = 0, sticky = W)
var1, var2 = IntVar(),IntVar()
Checkbutton(root, text = "Male", variable = var1).grid(row =1, sticky = W)
Checkbutton(root, text = "Female", variable = var2).grid(row =2, sticky = W)
Button(root, text = "Show", command = var_states).grid(row = 3, sticky = W)
Button(root, text = "Quit", command = root.quit).grid(row = 3, padx = 5,sticky = E)
root.mainloop()
root.destroy()

#############
from tkinter import *
class Checkbar(Frame):
   def __init__(self, parent=None, picks=[], side=LEFT, anchor=E):
      Frame.__init__(self, parent)
      self.vars = []
      for pick in picks:
         var = IntVar()
         chk = Checkbutton(self, text=pick, variable=var)
         chk.pack(side=side, anchor=anchor, expand=YES)
         self.vars.append(var)
   def state(self):
      return map((lambda var: var.get()), self.vars)
if __name__ == '__main__':
   root = Tk()
   lng = Checkbar(root, ['Python', 'Ruby', 'Perl', 'C++'])
   tgl = Checkbar(root, ['English','German'])
   lng.pack(side=TOP,  fill=X)
   tgl.pack(side=LEFT)
   lng.config(relief=GROOVE, bd=2)

   def allstates(): 
      print(list(lng.state()), list(tgl.state()))
   Button(root, text='Quit', command=root.quit).pack(side=RIGHT)
   Button(root, text='Peek', command=allstates).pack(side=RIGHT)
   root.mainloop()
   
#################################################################
from 


      
