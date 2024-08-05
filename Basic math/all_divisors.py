# link - https://bit.ly/3vzQ7yr
from typing import List

def printDivisors(n: int) -> List[int]:
    # Write your code here
    divisors = []
    for i in range(1,n+1):
        if (n%i==0):
            divisors.append(i)
    return divisors
    
    
