#!/usr/bin/env python
import urllib.request

req = urllib.request.Request('http://placekitten.com/100/200')
response = urllib.request.urlopen(req)

cat_img = response.read()

with open('cat_100_200','wb') as f:
	f.write(cat_img)
