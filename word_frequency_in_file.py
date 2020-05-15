frequency = {}

with open('C:\\Users\\User\\Downloads\\dataset_3363_3.txt') as text:
    s = text.read().lower().strip().split()
    s.sort()

    for word in s:
        count = frequency.get(word, 0)
        frequency[word] = count + 1

res = max(frequency, key=frequency.get)

print(res,' ',frequency[res])