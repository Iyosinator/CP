t = int(input())

for i in range(t):
    x,n = map(int,input().split())

    s = 0

    if n % 2 == 0:
        s = 0
    else:
        s = x
    print(s)    