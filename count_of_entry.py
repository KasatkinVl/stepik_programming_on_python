gen = 'abc'
modify = gen + ' '
i = 0
j = len(modify) - 1
count = 1
res = ''
while i < j:
    if modify[i + 1] == modify[i]:
        count += 1
    else:
        res += modify[i] + str(count)
        count = 1
    i += 1
print(res)

# genome = input()+' '
# s = 0
# n=genome[0]
# for i in genome:
#     if n!=i:
#         print(n + str(s), end = '')
#         s=0
#         n=i
#     s+=1