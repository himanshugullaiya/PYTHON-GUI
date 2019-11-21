import webbrowser
from tkinter import *

def web_search(text):
    link = "https://www.youtube.com/results?search_query="
    text = '+'.join(text.split(' '))
    link += text
    webbrowser.open(link)

class App:
    def __init__(self, master):
        self.frame = Frame(master, bg = '#fac170')
        self.frame.pack()

        self.label = Label(self.frame, text = "Welcome to Youtube Search", font = ('Monotype Corsiva', 16, 'bold'), bg = '#fac170')
        self.label.grid(row = 0, columnspan = 2, padx = 10, pady = 10)

        self.entry = Entry(self.frame, font = ('Arial',15), bd = 5, bg = '#ff9d85', width = 40)
        self.entry.focus_set()
        self.entry.grid(row = 1, columnspan = 2, padx = 10, pady = 10)

        self.button1 = Button(self.frame, text = "Try", fg = "black", bg = "white", command = self.make_obj)
        self.button1.grid(row = 2, column = 0 , padx = 5, pady = 5)

        self.button2 = Button(self.frame, text= "Quit", fg="black", bg="white", command = self.close)
        self.button2.grid(row = 2, column = 1 )

        master.bind('<Return>',self.make_obj)
        master.bind('<Escape>',self.close)

    def make_obj(self,event = 0):
        text = self.entry.get()
        print(text)
        web_search(text)
        self.frame.quit()

    def close(self, event = 0):
        self.frame.quit()



root = Tk()
app = App(root)
root.mainloop()
root.destroy()