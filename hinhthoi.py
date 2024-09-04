n=int(input())
if n % 2 == 1:
    for i in range(0,n,1):
        for j in range(0,2*n-1,1):
            if j == (n-i-1) or j == (n+i-1):
                print("*",end=' ')
            else:
                print(" ",end=' ')
        print()
    for i in range(n-2,-1,-1):
        for j in range(0,2*n-1,1):
            if j == (n-i-1) or j == (n+i-1):
                print("*",end=' ')
            else:
                print(" ",end=' ')
        print()
