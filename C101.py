n =int(input())
x =int(input())

def factorial(n):
    return n * factorial(n-1) if n>1 else 1

# print(factorial(0))

def exp(x):
    
    sum=0
    for i in range(0,n+1):
        answer= (x**i)/factorial(i)
        sum= sum+answer
    
    return sum  

print(exp(x))