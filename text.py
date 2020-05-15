new = ''
count = ''

with open('C:\\Users\\User\\Downloads\\dataset_3363_2.txt') as text:
    s = text.readline().strip()
    for i in range(len(s) - 1, -1, -1):
        if s[i].isdigit():
            count += s[i]
        else:
            num = int(count[::-1])
            q = s[i] * num
            new += q
            count = ''

with open('Ans.txt', 'w') as ans:
    ans.write(new[::-1])

print(new[::-1])
print()
print(s)
