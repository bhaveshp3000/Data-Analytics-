import urllib.request as urlr
import json

raw = urlr.urlopen("https://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=f7807e2b1c5e47568ed7e2d5e9cf1226")

print(raw.read())