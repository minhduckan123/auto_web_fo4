from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

url = "https://spin.fo4.garena.vn/"
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
driver.maximize_window()
driver.get(url)

with open("account.txt", "r") as f:
    read_file = [i.strip() for i in f.readlines()]
    
for i in read_file:
    username, password = i.split()
    username, password = username.strip(), password.strip()
        
    element = WebDriverWait(driver, 1800).until(EC.presence_of_element_located((By.XPATH, "//a[@href = '/user/login']")))
    element.click()
    
    driver.find_element_by_name("username").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    time.sleep(2)
    
    driver.find_element_by_id("confirm-btn").click()
    print("Logged in successfully")

print("Logout successfully")
print("\n-----Everything donewell!!-----\n")
