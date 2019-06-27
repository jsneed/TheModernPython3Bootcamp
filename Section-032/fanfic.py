from bs4 import BeautifulSoup
import requests 

url = "https://www.fanfiction.net/s/11915617/1/Flipped"

response = requests.get(url)
print('response.status_code -> ' + str(response.status_code))
if response.status_code == 200:
    html_str = response.text
else:
    html_str = ""

html_page = BeautifulSoup(html_str, "html.parser")

title = html_page.select("#profile_top b")[0].getText()
author = html_page.select("#profile_top a")[0].getText()
summary = html_page.select("#profile_top div.xcontrast_txt")[0].get_text()
completeText = html_page.select('#profile_top span.xgray.xcontrast_txt')[0].getText()
chapterText = html_page.select('#storytext')[0].getText()

print(title)
print(author)
print(summary)
print("\n\n\n")
#print(chapterText)

'''
chapterText = html_doc.css('#storytext').to_s

title = html_doc.css('#profile_top b')[0].content
author = html_doc.css('#profile_top a')[0].content
summary = html_doc.css('#profile_top div.xcontrast_txt')[0].content
completeText = html_doc.css('#profile_top span.xgray.xcontrast_txt')[0].content
'''