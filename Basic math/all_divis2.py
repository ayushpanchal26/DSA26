from typing import List

def printDivisors(n: int) -> List[int]:
    # Write your code here
    divisors = []
    for i in range(1,n+1):
        if (n%i==0):
            divisors.append(i)
    return divisors


# better code with better runtime
from typing import List
import math

def printDivisors(n: int) -> List[int]:
    divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    divisors.sort()  
    return divisors
