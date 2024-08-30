# ###link - https://bit.ly/3ppA6YJ
class Solution: 
    def select(self, arr, i):
        # code here 
        pass
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(0,n-1):
            min_index = i
            for j in range(i,n):
                if arr[j]<arr[min_index]:
                    min_index = j
            arr[min_index],arr[i] = arr[i],arr[min_index]

