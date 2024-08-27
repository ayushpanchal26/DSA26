# link - https://bit.ly/3LOkcBn
class solution:
  def printNos(self,n):
    if n<1:
      return 
    print(n,end=' ')
    self.printNos(n-1)
