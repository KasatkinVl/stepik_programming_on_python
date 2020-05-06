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
