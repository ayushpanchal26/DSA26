# link - HCF/GCD: https://bit.ly/3GB4Mj8
from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
def gcd(x,y):
    while(x>0 and y>0):
        if (x>y):
            x = x%y
        else:
            y = y%x
    if (x==0):
        print(f"{y}")
    else:
        print(f"{x}")

x = int(input())
y = int(input())

gcd(x,y)
