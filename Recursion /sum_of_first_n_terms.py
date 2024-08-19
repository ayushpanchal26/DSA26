# link - https://practice.geeksforgeeks.org/problems/sum-of-first-n-terms5843/1
# These is Functional recursive method.
def sumOfSeries(self,n):
  if n ==1:
    return 1
  return n**3+self.sumOfSeries(n-1)
  
