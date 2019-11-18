def squaresum(n):
    sm=0
    for i in range(1,n+1):
        sm=sm+(i*i)
    return sm
n=int(input('enter the number:'))
squaresum(n)
def sumsqare(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+i
    return(sum*sum)
sumsqare(n)
print(sumsqare(n))
print('result',sumsqare(n)-squaresum(n))
