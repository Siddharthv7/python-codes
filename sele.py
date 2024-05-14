from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

driver = webdriver.Chrome()  # Replace with your browser's WebDriver

search_query = "articles python"
url = f"https://www.google.com/search?q={search_query}"
driver.get(url)
# Inspect the search results to find the appropriate locators
links = []
results = driver.find_elements(By.XPATH,'//*[@id="search"]/div')
print(results)
for result in results[1]:
    link = result.get_attribute("href")
    links.append(link)

    # Close the browser
driver.quit()

for i, link in enumerate(links, start=1):
    print(f"{i}. {link}")