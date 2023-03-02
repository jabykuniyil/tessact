import requests as r

endpoint = "http://localhost:8000/blogs/1/"

item = r.get(endpoint)
print(item.json())

