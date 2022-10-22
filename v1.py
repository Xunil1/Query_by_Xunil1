import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def start_query(steps:int, mean:str, vendor_code:str):
    for i in range(steps):
        try:
            browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            browser.implicitly_wait(5)
            browser.maximize_window()
            browser.get('https://www.wildberries.ru/')
            browser.find_element(By.ID, 'searchInput').send_keys(mean)
            browser.find_element(By.ID, 'applySearchBtn').click()
            try_n = 1
            while True:
                try:
                    browser.find_element(By.XPATH, "//*[@id='" + vendor_code + "']/div/a").click()
                    time.sleep(random.randint(2,4))
                    print(i)
                    break
                except Exception as e:
                    browser.find_element(By.LINK_TEXT, str(try_n + 1)).click()
                    # elif try_n > 1:
                    #     browser.find_element(By.XPATH, "//*[@id='catalog']/div[1]/div/div[3]/div[6]/div/div/a[" + str(try_n + 1) + "]").click()
                    try_n += 1
            browser.close()
        except:
            print("!!!ERROR!!! PAUSE FOR 15 MINUTES !!!")
            time.sleep(900)


# st = int(input("Введите количество повторов запроса: "))
# query = input("Введите запрос: ")
# vendor_code = "c" + input("Введите артикул: ")
start_query(1000, "кальсоны мужские", "c105936923")