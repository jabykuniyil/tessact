import requests as r

endpoint = "http://localhost:8000/user/"

data = {
    "user_name": "jaby",
    "email_id": "jaby@gmail.com",
    "first_name": "ja",
    "last_name": "by"
}
res = r.post(endpoint, json=data)