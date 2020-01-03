import requests

#get data from the url
r = requests.get('https://en.wikipedia.org/wiki/List_of_highest-grossing_films')

#print content, useful for media
print(r.content)
#print text, useful for parsing
print(r.text)