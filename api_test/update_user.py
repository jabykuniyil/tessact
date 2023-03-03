import requests as r

endpoint = "http://localhost:8000/user/6/"

data = {
    "user_name": "None",
    "email_id": "muha@gmail.com",
    "first_name": "mooo",
    "last_name": "haaa",
    "password": "muhaa",
    "dob": "2000-02-10",
    "address": "dd",
    "phone_number": "381803011",
    "notify_user": True
}
res = r.put(endpoint, json=data)
print(res.json())
