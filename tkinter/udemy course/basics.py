# |:| Button - click |:|  Label - Any text |:| Entry - Text entry box 
from tkinter import *
from tkinter import messagebox
import random

# Functions

# Random Text Generation
texts = [chr(x) for x in range(ord('a'), ord('z')+1)]
def gen_rand_text():      
      rand_text = random.choice(texts)
      for x in range(3):
            rand_text += random.choice(texts)
      return rand_text


#.......... Button Click ..........#
def buttonclick_1():
#      messagebox._show("Message", "Button Clicked :)")
      labeltext.set('Cyan')
      label.config(bg = 'cyan')

def buttonclick_2():
#      messagebox._show("Message", "Button Clicked :)")
      labeltext.set('Yellow')
      label.config(bg = 'Yellow')

def buttonclick_3():
#      messagebox._show("Message", "Button Clicked :)")
      labeltext.set('grey')
      label.config(bg = 'grey')
      
#...................................#
      
def cleartext():
      entry.delete(0, END)
      
def showonlabel():
      labeltext.set(entry.get())
      
      
#..................#
root = Tk()
#..................#


#***************..LABEL...***********************
mylabel = Label(root, text = "My First Label")  # Label is a class 
mylabel.pack()

#....For bt_2, bt_3, bt_5.......#
labeltext = StringVar()
labeltext.set('-------')

label = Label(root, textvariable = labeltext)
label.pack()
#.............................#






# *****************...BUTTON.....*******************
# bt_1 = Button(root, text = "Click me", command = lambda : messagebox._show("Message", "Button Clicked :)")).pack()

#bt_2 = Button(root, text = "Click", command = lambda : labeltext.set(gen_rand_text())).pack()

#bt_3_1 = Button(root, text = "Surpise", command = buttonclick_1).pack()
#bt_3_2 = Button(root, text = "suprise", command = buttonclick_2).pack()
#bt_3_3 = Button(root, text = "suprise", command = buttonclick_3).pack()

#bt_4 = Button(root, text = "Clear Entry Box", command = cleartext).pack()

#bt_5 = Button(root, text = "Show entry box content", command = showonlabel).pack()



# **************...CHECKBUTTON...**************************
#Label(root, text = "Which is your favourite?").pack()
#Checkbutton(root, text = "Milk").pack()
#Checkbutton(root, text = "Apple Juice").pack()
#Checkbutton(root, text = "Mango Shake").pack()



#*****************...ENTRY...******************************

entry = Entry(root, bg = 'cyan', fg = 'black')
entry.pack()



#*****************.... RADIOBUTTON....************************
#radiobuttonval = IntVar()

#..........***...............
#strvar = StringVar()
#def setval():
#      temp = radiobuttonval.get()
#      tz = "Weather Selected: "+ str(temp)
#      strvar.set(tz)
#      
#
#Label(root, text = "What is your favourite Weather? ").pack()
#Radiobutton(root, text = 'Sunny', value = 1, variable = radiobuttonval).pack()
#Radiobutton(root, text = 'Rainy', value = 2, variable = radiobuttonval).pack()
#Radiobutton(root, text = 'Cloudy', value = 3, variable = radiobuttonval).pack()
#
#Button(root, text = "Show Radio Button Value", command = lambda : print(radiobuttonval.get())).pack()
##....................***.......................
#Button(root, text = "Check", command = setval).pack()
#l = Label(root, textvariable = strvar)
#l.pack()




root.mainloop()

