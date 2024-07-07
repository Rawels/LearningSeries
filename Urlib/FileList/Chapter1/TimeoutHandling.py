import requests

#link for using delay
link = "http://httpbin.org/delay/10"

try:
    #setting timeout in requests
    response = requests.get(url= link, timeout=5)
    print(response.status_code)
    #if response take too long then raise error
except requests.exceptions.Timeout as error:
    print(f"We have time out error {error}")