class gellany_number2word():

     def __init__(self, n = None):
              self.n = n

     def main(self):

                 arr = ['zero','one','two','three','four','five','six','seven','eight','nine']
                 
                 for i in self.n :
                       print(arr[int(i)], end =" ")

n = input()
#print(n)
print("Number Entered was : ", n)
print("Converted to word it becomes: ",end="")
gellany_number2word(n = n).main()
