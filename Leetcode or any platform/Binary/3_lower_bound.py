# link - https://bit.ly/3Cf398N
class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self,A,N,X):
        #Your code here
        low = 0 
        high = N-1
        ans = -1
        while low<=high:
            mid = (low+high)//2
            if A[mid] <= X:
                ans = mid
                low = mid+1
                
            else:
                high  = mid -1
        return ans