from tkinter import *
from flask import Flask, request, render_template
from flask import jsonify
import argparse

class gellany_number2word_all():

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

    def web(self):

              app = Flask(__name__)


              @app.route("/")

              def my_form():
                  return render_template('my-form.html')

              @app.route('/', methods=['POST'])

              def main():
                               n = request.form['text']
                               arr = ['zero','one','two','three','four','five','six','seven','eight','nine']

                               res = []
                               for x in n:
                                  res.append(arr[int(x)])

                               return jsonify(res)

              app.run(debug=True)


    

    def terminal(self):

                 n = input("Please enter a string:\n")
                 print("Number Entered was : ", n)
                 print("Converted to word it becomes: ",end="")

                 arr = ['zero','one','two','three','four','five','six','seven','eight','nine']
                 
                 for i in n :
                       print(arr[int(i)], end =" ")                       

    def gui(self):

              window = Tk()
              window.title("Welcome to gellany_number2word")
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

              


    def main(self):

              my_parser = argparse.ArgumentParser()
              my_parser.add_argument('--mode')
              args = my_parser.parse_args()
       
              if args.mode == 'web':
                           self.web() 
              elif args.mode == 'terminal':
                           self.terminal()  

              elif args.mode == 'gui':
                           self.gui()

              
              


gellany_number2word_all().main()






