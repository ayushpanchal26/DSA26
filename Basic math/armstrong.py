# Armstrong: https://bit.ly/3vBfkbD
def checkArmstrong(n):
    #write your code here !!!!!!!!!
    sum = 0
    original = n
    while(n>0):
        last_digit = n%10
        n = n//10
        sum = sum+(last_digit*last_digit*last_digit)
    return original == sum

    
