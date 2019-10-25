from tkinter import *
import random
root = Tk()

def get_table():
      for x in range(10):
            label_txt[x].set(str(entry.get())+ 'X' + str(9-x+1) + '=' + str(int(entry.get())*(9-x+1)))

def reset():
      for x in range(10):
            label_txt[x].set('------------------')
            entry.delete(0,END)
      
colors = ["pink", "gray70", "indian red", "pale green", "deep sky blue", "cyan", "yellow", "magenta"]

entry = Entry(root, font = ('Courier',15))
entry.pack()


list_labels = []
label_txt = []
for x in range(10):      
      tp = StringVar()
      tp.set('------------------')
      label_txt.append(tp)
      my_label = Label(root, textvariable = label_txt[x], font = ('Courier',20), bg = random.choice(colors), width = 10)
      list_labels.append(my_label)
      list_labels[x].pack(side = 'bottom')

Button(root, text = "Show Table", command = get_table, width = 10).pack(padx = 45, pady = 5, side = 'left')
Button(root, text = "Reset", command = reset, width = 10).pack(padx = 2, pady = 5, side = 'left')

root.mainloop()