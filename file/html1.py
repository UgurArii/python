from bs4 import urlllib
import BeautifulSoup
import urllib from bs4
response = urllib.request.urlopen('http://python-data.dr-chuck.net/known_by_Rona.html'
html_doc = response.read()
soup = BeautifulSoup(html_doc, 'html.parser')
print(html_doc[:700])
print("\n")
print (soup.title)
print(soup.title.string)
print(soup.a.string)

