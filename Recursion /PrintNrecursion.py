# link - https://bit.ly/3K2epHv
class Solution:    
    #Complete this function
    def printNos(self,N):
        #Your code here
    
        if N<1:
            return
        
        self.printNos(N-1)
        print(N,end=' ')
