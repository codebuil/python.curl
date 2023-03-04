import requests
import sys
url = 'https://www.microsoft.com'
argumentos = sys.argv
print ("\033c\033[44;30m")
if len(argumentos)>1 :
    url=argumentos[1]
    
response = requests.get(url)
print(response.content)