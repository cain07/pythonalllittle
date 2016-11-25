import urllib.request
import urllib.parse
import json
import time

while True:
	content = input('请输入需要翻译的内容(输入q!退出程序)')
	if content == 'q!':
		break


	url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=https://www.baidu.com/link'
	data = {}

	data['type'] = 'AUTO'
	data['i'] = content
	data['doctype'] = 'json'
	data['xmlVersion'] = '1.8'
	data['keyfrom'] = 'fanyi.web'
	data['ue'] = 'UTF-8'
	data['action'] = 'FY_BY_CLICKBUTTON'
	data['typoResult'] = 'true'

	data = urllib.parse.urlencode(data).encode('utf-8')

	req = urllib.request.Request(url,data)
	req.add_header('User-Agent','Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36')
	response = urllib.request.urlopen(url,data)


	html = response.read().decode('utf-8')

	target = json.loads(html)

	print(target['translateResult'][0][0]['tgt'])

	time.sleep(5)

