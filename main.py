import requests 
from bs4 import BeautifulSoup 


r = requests.get("https://www.google.com/search?q=") 
 
soup = BeautifulSoup(r.content, 'html.parser') 
 
for link in soup.find_all('a'): 
	print(link.get('href'))
