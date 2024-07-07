import requests

#GetWebsite = requests.get("https://www.linkedin.com/pulse/top-6-programming-languages-hackers-pentesters-arun-kl#:~:text=C%23%20is%20among%20the%20best,used%20in%20security%20tools%20automation.")
#.content for take out HTML
#.status_code for checking response status
#print(GetWebsite.content)
#print(GetWebsite.status_code)

#send data to HTTP endpoint
SendingData = {
    'name': "Peter",
    'message': "SpiderMan",
    'season': 4
}
#make post request json data in above
response = requests.post(url="http://httpbin.org/post", json= SendingData)
#see data content, the link in url is use for testing
print(response.json())