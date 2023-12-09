from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class PreferencePage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver


    CHANGE_PASSWORD_BUTTON = '//*[@id="region-main"]/div/div/div/div[1]/div/div/div/div[2]/a'
    CURRENT_PASSWORD_FIELD = '//*[@id="id_password"]'
    NEW_PASSWORD_FIELD = '//*[@id="id_newpassword1"]'
    REPEAT_NEW_PASSWORD_FIELD = '//*[@id="id_newpassword2"]'

    SAVE_CHANGE_BUTTON = '//*[@id="id_submitbutton"]'

    CONTINUES_BUTTON = '/html/body/div[2]/div[3]/div/div[2]/div/section/div/div[2]/form/button'

    CURRENT_PASSWORD_ERROR = '//*[@id="id_error_password"]'
    NEW_PASSWORD_ERROR = '//*[@id="id_error_newpassword1"]'
    REPEAT_PASSWORD_ERROR = '//*[@id="id_error_newpassword2"]'

    def change_password(self, current_password, new_password, repeat_new_password, screenshot_path):
        # Click on change password
        self.driver.find_element(By.XPATH, self.CHANGE_PASSWORD_BUTTON).click()
        time.sleep(5)

        # Enter current password
        if current_password != None:
            self.driver.find_element(By.XPATH, self.CURRENT_PASSWORD_FIELD).send_keys(current_password)
            time.sleep(2)

        # Enter new password
        if new_password != None:
            self.driver.find_element(By.XPATH, self.NEW_PASSWORD_FIELD).send_keys(new_password)
            time.sleep(2)

        # Repeat new password
        if repeat_new_password != None:
            self.driver.find_element(By.XPATH, self.REPEAT_NEW_PASSWORD_FIELD).send_keys(repeat_new_password)
            time.sleep(2)

        # Click login and wait for load
        self.driver.find_element(By.XPATH, self.SAVE_CHANGE_BUTTON).click()
        time.sleep(5)

        # Save screenshot
        self.driver.save_screenshot(screenshot_path)
        time.sleep(2)



    def change_password_success(self):
        try:
            self.driver.find_element(By.XPATH, self.CONTINUES_BUTTON).click()
            print("Result: Change password successfully.")
            return "Change password successfully."
        except:
            current_password_error = self.driver.find_element(By.XPATH, self.CURRENT_PASSWORD_ERROR).text
            if current_password_error != "" and current_password_error == "Invalid login, please try again":
                print("Result: Invalid login, please try again.")
                return "Invalid login, please try again."
            
            new_password_error = self.driver.find_element(By.XPATH, self.NEW_PASSWORD_ERROR).text
            if new_password_error != "" and (new_password_error == "The new password must be different than the current one" or new_password_error == "These passwords do not match"):
                print(f"Result: {new_password_error}.")
                return new_password_error + "."
            
            print("Result: Missing field.")
            return "Missing field."
