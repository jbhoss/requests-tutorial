import requests

#pass the parameters as a dictionary to reduce errors
payload = {'page':2, 'count':25}
r = requests.get('https://httpbin.org/get')

#get the response as a json file
#print(r.text)
#Remove the comment to see the response shown below
'''
Response without the parameters
{
  "args": {}, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.22.0"
  }, 
  "origin": "182.69.198.144, 182.69.198.144", 
  "url": "https://httpbin.org/get"
}
'''

#We are passing the parameters
r = requests.get('https://httpbin.org/get',params=payload)
print(r.text)

'''
Response with the parameters
{
  "args": {
    "count": "25", 
    "page": "2"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.22.0"
  }, 
  "origin": "182.69.198.144, 182.69.198.144", 
  "url": "https://httpbin.org/get?page=2&count=25"
}
'''