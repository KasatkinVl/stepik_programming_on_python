import requests

with open('C:\\Users\\User\\Downloads\\file.txt', encoding='utf-8') as text:
    url = text.readline().strip()

r = requests.get(url)
text = r.text.splitlines()


print(len(text))

#НЕЛЬЗЯ НАЗЫВАТЬ ФАЙЛЫ ИМЕНАМИ БИБЛИОТЕК