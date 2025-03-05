
import requests
r = requests.get("http://api.open-notify.org/iss-now.json")
print(r.status_code)
print(r.text)
