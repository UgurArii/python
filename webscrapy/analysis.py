from bs4 import BeautifulSoup
import requests

page = requests.get("http://www.arthurleej.com/e-love.html")
print(page)
print(page.content)

page2= requests.get("http://ariugur.com")
print(page2.content)

soup = BeautifulSoup(page.content, "html.parser")
print(soup.prettify())
"""

title = soup.find("u")
print(title)
print(title.get_text())

poem_text = soup.find_all("b")
for text in poem_text:
    print(text.get_text())
    
    # finding an element by specific attribute key-values
page = requests.get("https://github.com/Connor-SM")
soup = BeautifulSoup(page.content, "html.parser")
username = soup.find( "span", attrs={ "class" : "vcard-username" }
)       # find first span with this class
print(username)       # will show that element has class of vcard-­
print( username.get_text( ) )

"""

print(soup.children)

for child in list(soup.children):
    print(type(child))
    
html = list(soup.children)[2]
for section in html:
    print("\n\n Start of new section")
    print(section)  

head = list(html.children)[1]    
for item in head:
    print("\n\n Start of new section")
    print(item)  