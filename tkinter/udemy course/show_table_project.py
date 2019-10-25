from tkinter import *
import random

root = Tk()
colors = ['tomato', 'pale green', 'cyan', 'pink', 'peach puff', 'gold', 'orchid1','brown','oliveDrab1']

entry = Entry(root, bg = 'peach puff' , fg = 'red')
entry.pack()



list_labels = []
list_stringvar = []



Button(root, text = "Show Table", command = showtable).pack()

for x in range(10):
      label_text = StringVar()
      label_text.set('---------')
      list_stringvar.append(label_text)
      
for x in range(10):
      label = Label(root, textvariable = list_stringvar[x])
      label.config(bg = random.choice(colors), width = 15)
      label.pack()      
      list_labels.append(label)
      



def showtable():
      no = entry.get()
      if no:
            for i in range(1,11):
                  result = int(no)*i
                  table_string = str(no)+" X "+str(i)+" = "+str(result)
                  list_stringvar[i-1].set(table_string)
                  list_labels[i-1].config(bg = random.choice(colors))



      
root.mainloop()
