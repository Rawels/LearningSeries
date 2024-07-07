import requests
try:
    response = requests.get("http://httpbin.org/status/400")
    #raise for status is same as status_code
    response.raise_for_status()
    #the link is alway return for status 400 thus we try to catch that error though exceptions.HTTPError
except requests.exceptions.HTTPError as error:
    print(f"HTTP error {error}")