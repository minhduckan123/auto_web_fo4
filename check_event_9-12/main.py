from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chromium.options import ChromiumOptions
from selenium.webdriver.chrome.options import Options
import time


optios = Options
chromium_options = ChromiumOptions

optios.headless = True
chromium_options.headless = True

url = "https://spin.fo4.garena.vn/"
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver", optinons= chromium_options)
# driver.maximize_window()
driver.get(url)


with open("hello_text_01.txt", "r") as f:
    read_file = [i.strip() for i in f.readlines()]

for i in read_file:
    username, password = i.split()
    username, password = username.strip(), password.strip()

    driver.find_element_by_xpath("//a[@href = '/user/login']").click()

    driver.find_element_by_name("username").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    time.sleep(1)

    # Dang nhap
    driver.find_element_by_id("confirm-btn").click()

    # Chon muc nhiem vu
    element = WebDriverWait(driver, 1800).until(EC.presence_of_element_located(
        (By.XPATH, "//a[@class = 'animate__animated animate__tada animate__infinite']")))
    element.click()
    time.sleep(2)
    try:
        # Cap nhat nhiem vu
        driver.find_element_by_class_name("mission__action").click()
        driver.find_element_by_class_name("close").click()
    except:
        try:
            # Da cap nhat nhiem vu
            driver.find_element_by_class_name("close").click()
        except:
            # Nhiem vu chua hoan thanh
            element_close = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//button[@type = 'button']")))
            element_close.click()
            driver.find_element_by_class_name("close").click()
    
    # Dang xuat
    element_logout = WebDriverWait(driver, 1800).until(
        EC.presence_of_element_located((By.XPATH, "//a[@href='/user/logout']")))
    element_logout.click()

    print("{:<15} : {:<12}".format(account,password))
print("\n-----Everything donewell!!-----\n")
