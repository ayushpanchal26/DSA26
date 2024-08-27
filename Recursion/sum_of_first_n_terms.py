# link - https://practice.geeksforgeeks.org/problems/sum-of-first-n-terms5843/1
# These is Functional recursive method.
def sumOfSeries(self,n):
  if n ==1:
    return 1
  return n**3+self.sumOfSeries(n-1)
  
# optimal way to do these question is 
def sumOfSeries(self,n):
        #code here
        sum_n = n*(n+1)//2
        return sum_n**2
  # because in recursion method the time limit will be exceeded.
  

