import requests as r

endpoint = "http://localhost:8000/blogs/4?author=4"

item = r.delete(endpoint)
# print(item.json())

