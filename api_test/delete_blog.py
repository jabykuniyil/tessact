import requests as r

endpoint = "http://localhost:8000/blogs/2/"

item = r.delete(endpoint)
print(item.json())

