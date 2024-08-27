# Check Prime: https://bit.ly/3ZdiWOO
def check_prime(num):
    count = 0 
    if num<=1:
        return False

    for i in range(2,num):
        if num%i==0:
            return False
        
    return True
