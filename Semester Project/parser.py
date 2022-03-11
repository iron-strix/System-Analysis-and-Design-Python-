from urllib.request import urlopen
import re

#search
url = 'https://www.dictionary.com/browse/'
term = input("input a word to search: ").casefold()
url += term
#print(f"Searching {url} ...")

page = urlopen(url)

html_bytes = page.read()
html = html_bytes.decode("utf-8")

pattern = "<div class=\"default-content\">.*?<span class=\"luna-example"

match_results = re.search(pattern, html, re.IGNORECASE)

result = match_results.group()
result = re.sub("<.*?>", "", result) #remove HTML tags

result = result.replace("<span class=\"luna-example", "", 1)

print(result)