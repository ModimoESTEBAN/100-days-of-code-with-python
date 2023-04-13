import requests

url = "https://chat-server-d27s.onrender.com/api/app/profile"
post = "https://chat-server-d27s.onrender.com/api/user/validate"

r = requests.post(post, data={'username': '', 'email': '', 'password': ''})
j = r.json()
s = r.status_code
print(j)
print(s)

