import requests
import time

r = requests.get('https://yandex.ru/images/search?from=tabbar&text=mr%20robot')
print(r.text)
time.sleep(1)
r2 = requests.get('https://yandex.ru/images/search?from=tabbar&text=mr%20robot')
print(r2.text)
print(r.text == r2.text)