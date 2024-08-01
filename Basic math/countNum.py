# link - Count Digits: https://bit.ly/3X17nIr
def countDigits(n: int) -> int:
    # Write your code here
    count = 0 
    while(n>0):
        last = n%10
        count +=1
        n = n//10
    return count
