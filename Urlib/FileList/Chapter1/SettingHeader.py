import requests

auth_token = "somethingLikeToken"
addAuthToHeader = {
    'Authorization': auth_token
}
url = "http://httpbin.org/headers"
response =requests.get(url= url, headers= addAuthToHeader)
print(response.json())