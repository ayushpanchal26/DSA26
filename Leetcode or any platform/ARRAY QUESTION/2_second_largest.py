# link - https://bit.ly/3pFvBcN
class solution:
    def print2largest(self,arr):
        n = len(arr)
        if n == 0 and n ==1:
            return -1
        large = float('-inf')
        second_large = float('-inf')
        for i in range(n):
            large = max(large,arr[i])

        for i in range(n):
            if arr[i]> second_large and arr[i]!= large:
                second_large = arr[i]
            
        if second_large == float('-inf'):
            return -1
        
        return second_large
    
obj = solution()
arr = [1,2,3,4,5,3,2]
ans = print(f"second largest value = {obj.print2largest(arr)}")