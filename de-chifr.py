line1 = list(input())
line2 = list(input())
dic = dict(zip(line1,line2))

line3 = list(input())
line4 = list(input())


def chifr(str_to_chifr,dic):
    myString = ''
    x = list(str_to_chifr)
    for i in range(len(x)):
        x[i] = dic.get(x[i])
    myString = ''.join(x)
    return myString

def dechifr(str_to_dechifr,dic):
    myString = ''
    inv_map = {}
    x = list(str_to_dechifr)
    inv_map = {v: k for k, v in dic.items()}
    for i in range(len(x)):
        x[i] = inv_map.get(x[i])
    myString = ''.join(x)
    return myString

print(chifr(line3,dic))
print(dechifr(line4,dic))
# abcd
# *d%#
# abacabadaba
# #*%*d*%