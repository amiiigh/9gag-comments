import json
from tqdm import *
import requests

urls_file = open('urls.json')
urls_json_data = json.load(urls_file)
for url in tqdm(urls_json_data):
	commment_url = "http://comment-cdn.9gag.com/v1/cacheable/comment-list.json?appId=a_dd8f2b7d304a10edaf6f29517ea0ca4100a43d1b&url="+url['url']+"&count=1000&level=2"
	r = requests.get(commment_url)
	json_data = r.json()
	for c in json_data['payload']['comments']:
		display_name =c['user']['displayName']
		with open('users','aw') as outputfile:
			outputfile.write(display_name +'\n')