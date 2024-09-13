# link -  https://bit.ly/3A30Anw
class Solution:
    def merge(self,arr, l, m, r): 
        # code here
        temp = []
        left = l
        right = m+1
        while left<=m and right<=r:
            if arr[left]<=arr[right]:
                temp.append(arr[left])
                left+=1
            else:
                temp.append(arr[right])
                right+=1
                
        while left<=m:
            temp.append(arr[left])
            left+=1
        while right<=r:
            temp.append(arr[right])
            right+=1
        for i in range(l,r+1):
            arr[i] = temp[i-l]
                
    def mergeSort(self,arr, l, r):
        #code here
        if l >=r:
            return 
        m = (l+r)//2
        self.mergeSort(arr,l,m)
        self.mergeSort(arr,m+1,r)
        self.merge(arr,l,m,r)