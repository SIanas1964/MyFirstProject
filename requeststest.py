import requests

response = requests.get("https://www.google.com")

with open("example.html",'w') as file:
    file.write(response.text)


print(response.ok)          #The response successfully fulfilled the request or not
print(response.status_code) #Status code of the http request

###########
if not response.ok:
    raise Exception("GET failed with status code {}".format(response.status_code))
# OR
response.raise_for_status()
###########

#GET request example
p = {"search": "grey kitten",
         "max_results": 15}
response = requests.get("https://example.com/path/to/api", params=p)
print(response.request.url)
print(response.request.body)

#POST request example
p = {"description": "white kitten",
     "name": "Snowball",
     "age_months": 6}
response = requests.post("https://example.com/path/to/api", data=p)  #parameters are data
print(response.request.url)
print(response.request.body)

response = requests.post("https://example.com/path/to/api", json=p)  #parameters are json formated
print(response.request.url)
print(response.request.body)
