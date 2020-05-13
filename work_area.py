n = int(input())
a = [[0 for j in range(n)] for i in range(n)]
x = n
dx, dy = 0,0
count = 1

if n == 1:
    print(1)
else:

    while x != 0:

        for i in range(1):
            for j in range(n-1):
                a[i+dy][j] = count
                count += 1

        # for i in range(dy,n):
        #     for j in range(1):
        #         a[i][j-dx] = n + i
        #
        # for i in range(n-1,n):
        #     for j in range(n-2,-1,-1):
        #         a[i][j] = 3*n-2-j
        #
        # for i in range(n-2,0,-1):
        #     for j in range(1):
        #         a[i][j] = 3*n-2+(n-i-1)

        dx += 1
        dy += 1
        x -= n//2

    for i in range(n):
        print()
        for j in range(n):
            print(a[i][j], end=' ')

