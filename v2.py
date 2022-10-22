import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service


def init_query(mean:str, vendor_code:str):
    page = 1
    while True:
        try:
            browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            browser.implicitly_wait(5)
            browser.maximize_window()
            browser.get('https://www.wildberries.ru/')
            browser.find_element(By.ID, 'searchInput').send_keys(mean)
            browser.find_element(By.ID, 'applySearchBtn').click()

            while True:
                try:
                    browser.find_element(By.XPATH, "//*[@id='" + vendor_code + "']/div/a")
                    break
                except Exception as e:
                    browser.find_element(By.LINK_TEXT, str(page + 1)).click()
                    page += 1
            browser.close()
            return page
        except:
            print("!!!ERROR!!! PAUSE FOR 15 MINUTES !!!")
            time.sleep(60)


def start_query(steps:int, mean:str, vendor_code:str, card_page:int):
    step = 0
    for i in range(steps):
        try:
            browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            browser.implicitly_wait(10)
            browser.maximize_window()
            browser.get('https://www.wildberries.ru/')
            browser.find_element(By.ID, 'searchInput').send_keys(mean)
            browser.find_element(By.ID, 'applySearchBtn').click()
            if card_page <= 7 and card_page != 1:
                browser.find_element(By.LINK_TEXT, str(card_page)).click()
            elif card_page > 7:
                page = 7
                while page < card_page:

                    browser.find_element(By.LINK_TEXT, str(page)).click()
                    if page + 3 < card_page:
                        page += 3
                    else:
                        page = card_page
                browser.find_element(By.LINK_TEXT, str(page)).click()

            try:
                browser.find_element(By.XPATH, "//*[@id='" + vendor_code + "']/div/a").click()
                time.sleep(random.randint(2,4))
                random_active = 4#random.randint(1,2)
                if random_active == 1: # Просмотр характеристик
                    browser.find_element(By.CLASS_NAME, "j-parameters-btn").click()
                    time.sleep(random.randint(2, 4))
                elif random_active == 2: # Просмотр описания
                    browser.find_element(By.CLASS_NAME, "j-description-btn").click()
                    time.sleep(random.randint(2, 4))
                elif random_active == 3: # Просмотр изображения
                    browser.find_element(By.CLASS_NAME, "zoom-image-container").click()
                    time.sleep(random.randint(1, 3))
                    clicks = random.randint(1, 2)
                    while clicks > 0:
                        browser.find_element(By.CLASS_NAME, "swiper-button-next").click()
                        time.sleep(random.randint(1, 3))
                        clicks -= 1
                elif random_active == 4: # Просмотр описания
                    element = browser.find_element(By.CLASS_NAME, "user-activity__tabs")
                    action = ActionChains(browser)
                    action.move_to_element(element).click().perform()
                    time.sleep(8)
                    browser.find_element(By.CLASS_NAME, "comments__btn-all").click()
                    time.sleep(random.randint(3, 4))

                print(i)
            except Exception as e:
                return ["Error", i]
            browser.close()
            step = i
        except:
            print("!!!ERROR!!! PAUSE FOR 1 MINUTES !!!")
            time.sleep(60)
    return ["Done", step]


# st = int(input("Введите количество повторов запроса: "))
st = 1
# query = input("Введите запрос: ")
query = "швабра с отжимом и ведром"
# vendor_code = "c" + input("Введите артикул: ")
vendor_code = "c" + "99309021"
start_time = time.time()
while True:
    start_page = init_query(query, vendor_code)
    a = start_query(st, query, vendor_code, start_page)
    if a[0] == "Done":
        print("Done. Count:", a[1])
        break
    else:
        print("Error. Count:", a[1])
        st -= a[1]
end_time = time.time()
print("Time left:", end_time - start_time)