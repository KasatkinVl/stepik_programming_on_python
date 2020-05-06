a = [int(i) for i in input().split()]
res = []
sum = 0
if len(a) == 1:
    print(*a)
else:
    for i in range(len(a)):
        if i == 0:
            sum = a[i+1] + a[-1]
            res.append(sum)
        elif i == len(a)-1:
            sum = a[0]+a[i-1]
            res.append(sum)
        else:
            sum = a[i-1] + a[i+1]
            res.append(sum)
print(*res)

# a=[int(i) for i in input().split()]
# if len(a)>1:
#     for i in range(len(a)):
#         print(a[i-1]+a[i+1-len(a)])
# else:
#     print(a[0])