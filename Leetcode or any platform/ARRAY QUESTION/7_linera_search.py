# link - https://bit.ly/3KcpHcB
#User function Template for python3

class Solution:
    ##Complete this function
    def searchInSorted(self,arr, N, K):
        #Your code here
        for i in range(N):
            if arr[i]==K:
                return 1
        return -1