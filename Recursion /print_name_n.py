# link - https://bit.ly/3y2BiWz
def printGfg(self,n):
  if n == 0:
    return
  print(n-1)
  self.printGfg(n-1)
  
