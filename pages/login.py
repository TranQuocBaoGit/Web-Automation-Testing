from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class LoginPage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    USERNAME_FIELD = '//*[@id="username"]'
    PASSWORD_FIELD = '//*[@id="password"]'
    LOGIN_BUTTON = '//*[@id="loginbtn"]'

    ERROR_MESSAGE = '//*[@id="yui_3_18_1_1_1701826320109_28"]'

    USER_SETTING = '//*[@id="user-menu-toggle"]'
    LOGOUT_BUTTON = '//*[@id="carousel-item-main"]/a[9]'

    FORM = '//*[@id="login"]'

    def login(self, username, password, screenshot_path):
        # Clear username field
        self.driver.find_element(By.XPATH, self.USERNAME_FIELD).clear()
        time.sleep(2)

        # Enter username
        if username != None:
            self.driver.find_element(By.XPATH, self.USERNAME_FIELD).send_keys(username)
            time.sleep(2)

        # Enter password
        if password != None:
            self.driver.find_element(By.XPATH, self.PASSWORD_FIELD).send_keys(password)
            time.sleep(2)

        # Save test screenshot before process
        if screenshot_path != "skip":
            login_form = self.driver.find_element(By.XPATH, self.FORM)
            login_form.screenshot(screenshot_path)

        # Click login and wait for load
        self.driver.find_element(By.XPATH, self.LOGIN_BUTTON).click()
        time.sleep(5)



    def logout(self):
        # Click on user setting
        self.driver.find_element(By.XPATH, self.USER_SETTING).click()
        time.sleep(2)

        # Click logout
        self.driver.find_element(By.XPATH, self.LOGOUT_BUTTON).click()
        time.sleep(5)



    def login_success(self):
        # Return error message if login fail by checking if URL change
        if not (self.driver.current_url == "https://school.moodledemo.net/login/index.php"):
            print("Result: Login successfully")
        else:
            print("Result: Fail to login")
        return not (self.driver.current_url == "https://school.moodledemo.net/login/index.php")
