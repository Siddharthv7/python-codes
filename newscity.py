from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def get_daily_newsint():
    today = []
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    news_url = 'https://www.thehindu.com/news/cities/mumbai/' 

    driver.get(news_url)

    headlines = driver.find_elements(By.XPATH, '/html/body/section[3]/div/div[2]') 

    # Extract and print the headlines
    for headline in headlines:
        
        data= headline.text.split('\n')
        for st in data:
            if len(st)> 35:
                 today.append(st)
              
    with open(r"C:\my program\projects\localnews.txt", "w") as filenews:
                        for item in today:
                            filenews.write(item+"\n")
    # Close the browser
    
    
    driver.quit()
get_daily_newsint()
