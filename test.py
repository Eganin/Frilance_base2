import urllib

href = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQR-ON3xXc3ZhHixAsTj7lRbHSFEMWnYQwLJ528dKF2OYbw1VK9Kf3jfI9hUz4&s'

import requests

p = requests.get(href)
out = open("test.img", "wb")
out.write(p.content)
out.close()