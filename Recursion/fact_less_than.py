def function(list1,fact, i ,n):
    if fact>n:
        return list1
    list1.append(fact)
    return function(list1,fact*(i+1),i+1,n)


def factorialNumbers(n):
    list1=[]
    return function(list1,1,1,n)
        
print(factorialNumbers(55))