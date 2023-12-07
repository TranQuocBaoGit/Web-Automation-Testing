from utilities.read_xl import read_data_from_excel
from pages.login import LoginPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.process_image import crop_and_replace_image
import time

# This file is only for testing certain function

# value = read_data_from_excel("testdata/login.xlsx","Sheet1")
# print(value)

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)

driver.get("https://school.moodledemo.net/login/index.php")
driver.maximize_window()

# Login with manager priviledge
login_page = LoginPage(driver)
login_page.login("manager", "moodle", "skip")

driver.get("https://school.moodledemo.net/admin/search.php#linkusers")
time.sleep(5)

driver.find_element(By.XPATH, '//*[@id="linkusers"]/div/div[2]/div[2]/ul/li[3]/a').click()
time.sleep(5)

driver.execute_script("window.scrollTo(0, 200);")

driver.save_screenshot('test.png')

crop_and_replace_image('./test.png', 0.15, 0.17, 0.5, 0.9)

input("Enter an word to end...")
driver.close()