# Write a Python Program to create the dataframe and perform Boolean Indexing on it.
import pandas as pd
def index1():
      print(df.loc[True])
def index2():
      print(df.loc[False])

Days=['Monday','Tuesday','Wednesday','Thursday','Friday']
Classes=[1,2,3,4,5]
dc={'Days':Days,'No.Of  Days':Classes}
df=pd.DataFrame(dc,index=[True,False,True,False,True])
print(df)

print("-----------------Main Menu------------------")
print("1 Display all record with TRUE index")
print("2 Display all record with FALSE index")
while 1:
      n=int(input("Enter your  Choice(1,2):  "))
      if n==1:
            print("All records with TRUE index are")
            index1()
      elif n==2:
            print("All record with FALSE index are ")
            index2()
      else:
            print("Your choice is Wrong")
      ch=input("Y/N : ")
      if ch=='n' or ch=='N':
            print("Bye")
            break
