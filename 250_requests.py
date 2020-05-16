import requests

flag = []

with open('C:\\Users\\User\\Downloads\\dataset_3378_3.txt', encoding='utf-8') as text:
    url = text.readline().strip()
r = requests.get(url)
text = r.text
print(text)

while flag != ['We']:
    url1 = 'https://stepic.org/media/attachments/course67/3.6.3/'+text
    r = requests.get(url1)
    text = r.text
    s = text.strip().split()
    flag = s[0]
    print(text)

