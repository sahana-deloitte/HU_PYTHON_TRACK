n = 5
a=0
for i in range(1, n+1):
    for j in range(1, (n - i) +1):
        print(end=' ')
    while a!=(2*i-1):
        print('*', end='')
        a=a+1
    a=0

    print()

k=1
a=1

for i in range(1,n):
    for j in range(1,k+1):
        print(end=' ')
    k=k+1

    while a<=(2*(n-i)-1):
        print('*', end='')
        a=a+1
    a=1
    print()











