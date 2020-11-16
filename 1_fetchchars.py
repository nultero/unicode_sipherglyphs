from bs4 import BeautifulSoup
import requests
import json

searches = [ #may not be all of the searches I used
    "dot", 
    "circle",
    "old",
    "angle",
    "ogham",
    "ethiopic",
    "rejang",
    "coptic",
    "nordic",
    "chakma",
    "tifinagh",
    "arrow",
    "fork",
    "straight",
    "line", 
]

for i in searches:
    page = requests.get(f"https://unicode-search.net/unicode-namesearch.pl?term={i}")
    soup = BeautifulSoup(page.content, 'html.parser')
    data = soup.findAll("td", {"class": "character"})
    clean = {}
    for k,v in enumerate(data):
        add = {k:v.text}
        clean.update(add)

with open('cipher.json', 'w') as output:
    json.dump(clean, output)
print("Confirmed data exfil y" + ("e" * 50))