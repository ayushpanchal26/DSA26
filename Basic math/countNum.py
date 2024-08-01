# link - Count Digits: https://bit.ly/3X17nIr
def countDigits(n: int) -> int:
    # Write your code here
    count = 0 
    while(n>0):
        last = n%10
        count +=1
        n = n//10
    return count

# another method ---> for better runtime and memory graph 
import math 
def countDigits(n: int) -> int:
    # Write your code here
    count = int(math.log10(abs(n))+1)
    return count

    
