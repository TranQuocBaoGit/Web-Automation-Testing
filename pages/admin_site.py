from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.process_image import crop_and_replace_image
import time


class AdminSitePage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    ADD_USER_BUTTON = '//*[@id="linkusers"]/div/div[2]/div[2]/ul/li[3]/a'
    USERNAME_FIELD = '//*[@id="id_username"]'
    NEW_PASSWORD_CLICK = '//*[@id="fitem_id_newpassword"]/div[2]/span/a[1]'
    NEW_PASSWORD_FIELD = '//*[@id="id_newpassword"]'
    FNAME = '//*[@id="id_firstname"]'
    LNAME = '//*[@id="id_lastname"]'
    EMAIL = '//*[@id="id_email"]'
    CREATE_USER_BUTTON = '//*[@id="id_submitbutton"]'

    FORM = '//*[@id="id_moodlecontainer"]'

    def add_user(self, username, new_password, fname, lname, email, screenshot_path):
        # Click add user
        self.driver.find_element(By.XPATH, self.ADD_USER_BUTTON).click()
        time.sleep(5)

        # Scroll down a bit for a entire form
        self.driver.execute_script("window.scrollTo(0, 200);")
        time.sleep(2)

        # Enter username
        if username != None:
            self.driver.find_element(By.XPATH, self.USERNAME_FIELD).send_keys(username)
            time.sleep(2)

        # Enter new password
        if new_password != None:
            # Click to add new password
            self.driver.find_element(By.XPATH, self.NEW_PASSWORD_CLICK).click()
            time.sleep(2)
            # Input new password
            self.driver.find_element(By.XPATH, self.NEW_PASSWORD_FIELD).send_keys(new_password)
            time.sleep(2)

        # Enter first name
        if fname != None:
            self.driver.find_element(By.XPATH, self.FNAME).send_keys(fname)
            time.sleep(2)

        # Enter last name
        if lname != None:
            self.driver.find_element(By.XPATH, self.LNAME).send_keys(lname)
            time.sleep(2)

        # Enter email name
        if email != None:
            self.driver.find_element(By.XPATH, self.EMAIL).send_keys(email)
            time.sleep(2)

        # Scroll down to bottom
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

        # Click create user and wait for load
        self.driver.find_element(By.XPATH, self.CREATE_USER_BUTTON).click()
        time.sleep(5)

        if screenshot_path != "skip":
            self.driver.save_screenshot(screenshot_path)

            # Process image to crop only useful part
            if self.driver.current_url == "https://school.moodledemo.net/admin/user.php":
                crop_and_replace_image(screenshot_path, 0, 0.15, 1, 0.5)
            else:
                crop_and_replace_image(screenshot_path, 0.2, 0.1, 0.8, 1)
            time.sleep(5)



    def create_user_success(self):
        # Return error message if create user fail by checking if URL change
        if "https://school.moodledemo.net/admin/user.php" in self.driver.current_url:
            print("Result: Create new user successfully")
        else:
            print("Result: Fail to create new user")
        return ("https://school.moodledemo.net/admin/user.php" in self.driver.current_url)
