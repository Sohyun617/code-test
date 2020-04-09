n =int(input()) #A,B,C 문제에 따라 n값 지정, A: n=2, B: n=1, C: n=0

o=2 # 사탕이 들어있는 cylinder갯수
x=4 # 사탕이 들어있지 않은 cylinder 갯수
def pick(n):
    if n == 2:
        
        return o/(o+x) * (o-1)/(o+x-1)

    if n == 1:
        return o/(o+x) * x/(o+x-1) + x/(o+x) * o/(o+x-1) 

    if n == 0:
        return x/(o+x) * (x-1)/(o+x-1) * (x-2)/(o+x-2) * (x-3)/(o+x-3)
#print(pick(2))
#print(pick(1))
#print(pick(0))
print(pick(n))