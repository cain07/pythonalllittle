import urllib.request
import random

url = 'http://www.whatismyip.com.tw/'

proxy_support = urllib.request.ProxyHandler({'http':'182.36.176.118:8888'})

opener = urllib.request.build_opener(proxy_support)

urllib.request.install_opener(opener)

response = urllib.request.urlopen(url)

html = response.read().decode('utf-8')

print(html)
