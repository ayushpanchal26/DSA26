class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        orignal = x
        rev = 0
        while x>0:
            last = x%10
            rev = rev*10+last
            x = x//10
            
        return rev

# https://leetcode.com/problems/reverse-integer/
# Reverse Number: https://bit.ly/3vCeBXS

N  = int(input())
rev_num = 0
while(N>0):
    last_digit = N%10
    N = N//10
    rev_num = (rev_num*10)+last_digit

print(rev_num)

