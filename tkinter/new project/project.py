from tkinter import *
from PIL import Image, ImageTk
root = Tk()


#..........................Buttons  Details.................................#
border = 15
button_color = 'indian red'
#..........................X IMAGE.......................................#

frames_X = [PhotoImage(file='x.gif',format = 'gif -index %i' %(i)) for i in range(40)]

for x in range(40):
      frames_X[x] = frames_X[x].subsample(5)
      
def ab_X(x,y,ind):

      bt_count[x][y] += 1
      update_X(x,y,ind)
      
def update_X(x,y,ind):
#    if ind == 39:
#          ind = 1
    frame = frames_X[ind]    
    if bt_count[x][y] == 1:
          buttons[x][y].config(image=frame)
    else:
          buttons[x][y].config(image=frame, state = 'disabled')  
    buttons[x][y].grid(row = x, column = y, ipadx = 0, ipady = 0)    
    ind += 1
    k = 1
    root.after(20, update_X,x,y,ind)


#...........................O IMAGE......................................#
frames_O = [PhotoImage(file='rotate.gif',format = 'gif -index %i' %(i)) for i in range(20)]

for x in range(20):
      frames_O[x] = frames_O[x].subsample(4)
      
def ab_O(x,y,ind):
      
      bt_count[x][y] += 1
      update_O(x,y,ind)

def update_O(x,y,ind):
#    if ind == 19:
#          ind = 1
    frame = frames_O[ind]
    ind += 1
    if bt_count[x][y] ==1:
          buttons[x][y].config(image=frame)
    else:
          buttons[x][y].config(image=frame, state = 'disabled')
    buttons[x][y].grid(row = x, column = y, ipadx = 8, ipady = 24)
    root.after(60, update_O,x,y,ind)

#............................................................................#
    

#............................FRONT END IMPLEMENTATION CODE................................#
buttons = [[],[],[]]
bt_count = [[],[],[]]
bt_text = [[],[],[]]
for x in range(3):
      for y in range(3):
#            tp_text = StringVar()
            bt_text[x].append(StringVar())
            bt_text[x][y].set("")
            if ((x+y)%2 == 0 and (x!=1 and y!=1)):
                  color = "white"
                  tp_button = Button(root, textvariable = bt_text[x][y], padx = 82.2, pady = 82.2,highlightthickness = 10, bd = 5, bg = color,  command = lambda x=x,y=y: ab_X(x,y,0))#ldefault parameter x=x to avoid late binding
                  tp_button.grid(row = x, column = y, ipadx = 13, ipady = 0)
                  buttons[x].append(tp_button)
                  bt_count[x].append(0)
            else:
                  color = "turquoise"
                  tp_button = Button(root, textvariable = bt_text[x][y], padx = 82.2, pady = 82.2,bd = border, bg = color,  command = lambda x=x,y=y: ab_O(x,y,0))
                  tp_button.grid(row = x, column = y, ipadx = 13, ipady = 0)
                  buttons[x].append(tp_button)
                  bt_count[x].append(0)
            
#................................................................................#
#................................BACKEND IMPLEMENTATION CODE...........................#

root.mainloop()



