import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def init_query(mean:str, vendor_code:str):
    page = 1
    while True:
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        try:
            browser.implicitly_wait(5)
            browser.maximize_window()
            browser.get('https://www.wildberries.ru/')
            browser.find_element(By.ID, 'searchInput').send_keys(mean)
            browser.find_element(By.ID, 'applySearchBtn').click()

            while True:
                try:
                    browser.find_element(By.XPATH, "//*[@id='" + vendor_code + "']/div/a")
                    print("find")
                    break
                except Exception as e:
                    browser.find_element(By.LINK_TEXT, str(page + 1)).click()
                    page += 1
            browser.close()
            return page
        except:
            print("!!!ERROR!!! PAUSE FOR 15 MINUTES !!!")
            time.sleep(60)
            browser.close()


start_page = init_query("кальсоны мужские", "c105936923")
print(start_page)