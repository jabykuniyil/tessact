import requests as r

endpoint = "http://localhost:8000/blogs/"

data = {
    "user_name": "jy",
    "email_id": "by@gmail.com",
    "first_name": "jaa",
    "last_name": "bddy",
    "password": "dd"
}
res = r.post(endpoint, json=data)
