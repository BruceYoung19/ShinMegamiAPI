import requests
import json
from bs4 import BeautifulSoup

list_of_types=[]

url = "https://megamitensei.fandom.com/wiki/List_of_Shin_Megami_Tensei_Demons"
response = requests.get(url)
soup = BeautifulSoup(response.content,"html.parser")

for headers in soup:
    list_of_types.append(headers.a['title'])

print(list_of_types)
