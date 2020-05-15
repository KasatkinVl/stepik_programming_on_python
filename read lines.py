sum_of_I_course = 0
sum_of_II_course = 0
sum_of_III_course = 0
s = []

with open('C:\\Users\\User\\Downloads\\dataset_3363_4.txt', encoding='utf-8') as text:
    for line in text:
        s.append(line.strip().split(';'))
    print(s)

    for i in range(len(s)):
        sum_of_I_course += int(s[i][1])
        sum_of_II_course += int(s[i][2])
        sum_of_III_course += int(s[i][3])
        print((int(s[i][1]) + int(s[i][2]) + int(s[i][3])) / 3)

middle_I = sum_of_I_course / len(s)
middle_II = sum_of_II_course / len(s)
middle_III = sum_of_III_course / len(s)
print(middle_I, middle_II, middle_III)
