import requests

with open('C:\\Users\\User\\Downloads\\dataset_3378_3.txt', encoding='utf-8') as text:
    url = text.readline().strip()

r = requests.get(url)
text = r.text.splitlines()


print(len(text))

