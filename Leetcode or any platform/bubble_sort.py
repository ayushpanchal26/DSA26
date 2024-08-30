# link - https://bit.ly/3w6yQx8
class Solution:
    #Function to sort the array using bubble sort algorithm.
    def bubbleSort(self,arr, n):
        # code here
        didswap = 0
        for i in range(n,-1,-1):
            for j in range(0,i-1):
                if arr[j]>arr[j+1]:
                    arr[j+1],arr[j] = arr[j],arr[j+1]
                    didswap = 1
                    
            if didswap == 0:
                break
                