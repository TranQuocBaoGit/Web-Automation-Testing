from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class ProfilePage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    EDIT_PROFILE_BUTTON = '//*[@id="region-main"]/div/div/div[2]/section[1]/div/ul/li[1]/span/a'

    FIRST_NAME_FIELD = '//*[@id="id_firstname"]'
    LAST_NAME_FIELD = '//*[@id="id_lastname"]'
    EMAIL_FIELD = '//*[@id="id_email"]'
    CANCEL_EMAIL_CHANGE_BUTTON = '/html/body/div[3]/div[3]/div/div[2]/div/section/div/form/fieldset[1]/div[2]/div[3]/div[2]/div[1]/a'
    
    UPDATE_BUTTON = '//*[@id="id_submitbutton"]'

    def edit_profile(self, first_name, last_name, email, screenshot_path):
        # Click on change password
        self.driver.find_element(By.XPATH, self.EDIT_PROFILE_BUTTON).click()
        time.sleep(5)

        # Enter first name
        self.driver.find_element(By.XPATH, self.FIRST_NAME_FIELD).clear()
        time.sleep(2)
        if first_name != None:
            self.driver.find_element(By.XPATH, self.FIRST_NAME_FIELD).send_keys(first_name)
            time.sleep(2)

        # Enter last name
        self.driver.find_element(By.XPATH, self.LAST_NAME_FIELD).clear()
        time.sleep(2)
        if last_name != None:
            self.driver.find_element(By.XPATH, self.LAST_NAME_FIELD).send_keys(last_name)
            time.sleep(2)

        # Repeat email
        self.cancel_email_change()
        self.driver.find_element(By.XPATH, self.EMAIL_FIELD).clear()
        time.sleep(2)
        if email != None:
            self.driver.find_element(By.XPATH, self.EMAIL_FIELD).send_keys(email)
            time.sleep(2)

        # Click update and wait for load
        self.driver.find_element(By.XPATH, self.UPDATE_BUTTON).click()
        time.sleep(10)

        # Save screenshot
        self.driver.save_screenshot(screenshot_path)
        time.sleep(2)


    def cancel_email_change(self):
        try:
            self.driver.find_element(By.XPATH, self.CANCEL_EMAIL_CHANGE_BUTTON).click()
            time.sleep(10)
        except:
            pass

    def edit_profile_success(self):
        if "https://school.moodledemo.net/user/edit.php" == self.driver.current_url:
            print("Result: Edit profile successfully.")
            return True
        print("Result: Edit profile fail.")
        return False
