"""Write a menu driven program to calculate :
Area of circle [A=πr2]
Area of squire [A=a*a]
Area of rectangle [A=l*b]"""
def circle(r):
      return 3.14*r**2
def square(s):
      return s**2
def rectangle(l,b):
      return l*b

while 1:
      print('-'*50)
      print("----------------Main Menu-----------------")
      print("Type 1 for calculate Area of circle [A=π*r^2]")
      print("Type 2 for calculate Area of squire [A=a*a]")
      print("Type 3 for calculate Area  of  rectangle [A=l*b]")
      print('-'*50)
      n=int(input("Enter Your choice[1,2,3] :-"))
      if n==1:
            r=float(input("Enter value of radius of circle :- "))
            A= circle(r)
            print("Area of Circle is ",A,"unit^2")
      elif n==2:
            s=float(input("Enter value of side of square :- "))
            A=square(s)
            print("Area of Square is ",A,"unit^2")
      elif n==3:
            l=float(input("Enter value of lenght of rectangle :- "))
            b=float(input("Enter value of breath of rectangle :- "))
            A=rectangle(l,b)
            print("Area of Rectangle is ",A,"unit^2")
      else:
            print("Please enter correct option")
      ch=input("Do you want to go back to Main Menu[Y/N] : ")
      if ch=='n' or ch=='N':
            print("Bye")
            break
                  
