##from tkinter import *
##from PIL import Image, ImageTk
##root = Tk()
##
##photo = Image.open("1.png")
##photo = photo.resize((200,200), Image.ANTIALIAS)
##img = ImageTk.PhotoImage(photo)
##
##img3 = PhotoImage(file = 'cross.gif')
##
##photoo = Image.open("submit.png")
##photoo = photoo.resize((200,200), Image.ANTIALIAS)
##img1 = ImageTk.PhotoImage(photoo)
##
##img3_1 = Image.open("cross.gif")
##img3_tk = ImageTk.PhotoImage(img3_1)
##lbl = Label(root, image = img3)
##lbl.pack()
#
#from tkinter import *
#import time
#import os
#root = Tk()
#from PIL import Image, ImageTk, GifImagePlugin
##no = 50
##for x in range(50):
##      try:
##            frames = [PhotoImage(file='o_2.gif',format = 'gif -index %i' %(i)) for i in range(no)]
##      except:
##             print(no)
##             no -= 1
##      else:           
##             break
#
#imageObject = Image.open("rotate.gif")
#
#print(imageObject.is_animated)
#
#print(imageObject.n_frames)
#
#frames = []
#
## Display individual frames from the loaded animated GIF file
#
#for frame in range(0,imageObject.n_frames):
#
#    frames.append(imageObject.seek(frame))
#
#
#
#def update(ind):
#
#    frame = frames[ind]
#    ind += 1
#    label.configure(image=frame)
#    root.after(100, update, ind)
#label = Label(root)
#label.pack()
#root.after(0, update, 0)
#
#
#
#
##def on_enter(e):
##    myButton['background'] = 'indian red'
##
##def on_leave(e):
##    myButton['background'] = 'SystemButtonFace'
##
##
##myButton = Button(root, image = img, command = new)
##myButton.grid()
##
##
##myButton.bind("<Enter>", on_enter)
##myButton.bind("<Leave>", on_leave)
#
#root.mainloop()
#
def abc(x):
      for a in range(x):
            if a==x-2:
                  return tt(a)
def tt(x):
      print(x)
      
abc(8)
      
from tkinter import *
root = Tk()
buttons = [[],[],[]]
bt_text = [[],[],[]]
for x in range(3):
      for y in range(3):
#            tp_text = StringVar()
            bt_text[x].append(StringVar())
            bt_text[x][y].set("HUNNY")
            if ((x+y)%2 == 0 and (x!=1 and y!=1)):
                  color = "white"
            else:
                  color = "turquoise"
            tp_button = Button(root, textvariable = bt_text[x][y], padx = 82.2, pady = 82.2,bd = border, bg = color, command = None)
            tp_button.grid(row = x, column = y, ipadx = 0, ipady = 0)
            buttons[x].append(tp_button)


root.mainloop()
