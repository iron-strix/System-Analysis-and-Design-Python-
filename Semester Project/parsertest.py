#1 libraries needed
import urllib.request
import urllib.parse 
import re 

#2 search   
url = 'https://analyticsindiamag.com/'
values = {'s':'Web Scraping', 
          'submit':'search'} 

#3 parse
data = urllib.parse.urlencode(values) 
data = data.encode('utf-8') 
req = urllib.request.Request(url, data) 
resp = urllib.request.urlopen(req) 
respData = resp.read() 

#4 extract using regular expressions
document = re.findall(r'<p>(.*?)</p>',str(respData)) 
   
for line in document: 
    print(line) 