# Creating Multiplication Table :-

import math

class computation:
  
  def __init__(self,n):
    self.n = n
  
  def Tablemult(self):
    
    for i in range(2, self.n+1):
      print("\n\nMULTIPLICATION TABLE OF {}: \n".format(i))
      
      for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")

n = int(input())
p = computation(n)
p.Tablemult()
