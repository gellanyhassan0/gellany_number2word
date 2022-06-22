from tkinter import *

class gellany_number2word_tk():

    def __init__(self):
          pass

    def clicked(self):

              res = "Welcome to " + txt.get()
              lbl.configure(text= res)

    def number_word(self):

              arr = ['zero','one','two','three','four','five','six','seven','eight','nine']
              res = []
              for x in (txt.get()):
                    res.append(arr[int(x)])
                    
              lbl.configure(text= res)
                      

    def main(self):

              window = Tk()
              window.title("Welcome to LikeGeeks app")
              window.geometry('350x200')
         
              global lbl
              lbl = Label(window, text="Number Entered was")
              lbl.grid(column=0, row=0)
    
              global txt
              txt = Entry(window,width=10)
              txt.grid(column=1, row=0)
              
              btn = Button(window, text="Click Me", command=self.number_word)
              btn.grid(column=2, row=0)
              window.mainloop()

gellany_number2word_tk().main()