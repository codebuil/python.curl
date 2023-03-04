import requests
import sys
url = 'https://www.microsoft.com'
argumentos = sys.argv
if len(argumentos)>1 :
    url=argumentos[1]
    print (argumentos[1])
response = requests.get(url)
print(response.content)