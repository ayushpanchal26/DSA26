# Armstrong: https://bit.ly/3vBfkbD
def checkArmstrong(n):
    #write your code here !!!!!!!!!
    sum = 0
    length_of_n = len(str(n))
    original = n
    while(n>0):
        last_digit = n%10
        n = n//10
        sum = sum+(last_digit**length_of_n)
    return original == sum

    

    
