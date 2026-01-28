# link  - https://www.geeksforgeeks.org/problems/count-digits5716/1
def evenlyDivides (self, N):
        # code here
        count = 0 
        original_num = N
        while(N>0):
            last_digit = N%10
            N = N//10
            if last_digit!=0 and  original_num %last_digit ==0:
                count+=1
            
        return count
