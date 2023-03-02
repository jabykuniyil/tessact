import requests as r

endpoint = "http://localhost:8000/blogs/1/"

data = {'title': 'first edit pinnem', 'blog_content': 'ff edit', 'media_url': 'dd edit', 'created_by': 4,
        'created_at': '2023-03-02T19:29:00Z'}

res = r.put(endpoint, json=data)

