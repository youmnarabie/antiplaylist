from urllib.request import urlopen
from bs4 import BeautifulSoup

quote_page = 'http://everynoise.com/engenremap-neomellow.html'
page = urlopen(quote_page)
soup = BeautifulSoup(page, 'html.parser')

for div in soup.findAll('div', attrs={'id':'mirror'}):
    print(div.text)
#print(soup.find_all("div")[3])
#print(list(list(soup.children)[0]))


#name_box = soup.find('div', id_ = "mirror")



# lala = soup.select('div[id^=mirror]')
# print(type(lala[0]))
# #tootoo = name_box.find("div", class_ = "canvas")
# print(soup.prettify())
# #name_box = name_box.text.strip()
# print(name_box)