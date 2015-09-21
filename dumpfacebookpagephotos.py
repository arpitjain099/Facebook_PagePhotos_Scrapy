import urllib2
import requests
import codecs 
import csv
import json
import os
import sys
if not os.path.exists(sys.argv[2]+'/'):
    os.makedirs(sys.argv[2]+'/')

after=sys.argv[1]
r=requests.get("REPLACE_THIS_FRAGMENT_WITH_THE_RESPONSE_YOU_GET_IN_DEVELOPER_CONSOLE_BY_RUNNING_THE_INDEX_DOT_HTML_FILE")
#Example fragment for above: https://graph.facebook.com/v2.3/1423830694520861/photos?access_token=CAAHqcxGGr7oBAIfokIHmBs514tjsCem2idlVQoF8TVTpQgtgnDssH8kgeuiDJSYIy563ccLGOo0j6ckLg29YGeo0CqhhkZBymno8WAZBvIIA1Jf0vLKB8fZBRAk46WI6lP9zeBPMTuG7RwCFV5FUM1wor9EpFgAS9ZA3x8f8ZBSqDByNGaUHlII29fslrNsdQQTwmh9f0O4ZAA1esWkKLWw1g9hJcLcMcZD&pretty=0&type=uploaded&limit=25&after=MTY3ODE0MDEzOTA4OTkxNAZDZD


response = r.content
html = response
d=json.loads(html)
#print d['paging']
curr=d['paging']['previous']
ahead=d['paging']['next']
with open(sys.argv[2]+'csv.csv', 'a+') as csvfile:
	fieldnames = ['url', 'context','timestamp']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()
	while(ahead):
		#response=urllib2.urlopen(curr)
		r=requests.get(curr)
		response=r.content
		html = response
		d=json.loads(html)
		for i in d['data']:
			t=""
			if 'name' in i:
				t=i['name'].encode("utf-8")
			writer.writerow ({'url': str(i['images'][0]['source']),'context': t, 'timestamp':i['updated_time']})
		curr=ahead
		ahead=d['paging']['next']
#fi.close()