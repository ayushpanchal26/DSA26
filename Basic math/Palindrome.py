# https://leetcode.com/problems/palindrome-number/
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        orignal = x
        reverse = 0
        while(x>0):
            last = x%10
            x = x//10
            reverse = (reverse*10)+last
            
        return orignal == reverse
        


 
# https://leetcode.com/problems/palindrome-number/
n=int(input())  
orignal = n
reverse = 0 
while(n>0):
    last_digit = n%10
    n = n//10
    reverse = (reverse*10)+last_digit

if orignal == reverse:
    print('true')
else:
    print('false')
