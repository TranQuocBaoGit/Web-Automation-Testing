from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import os


class AsmPage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    ASM_1 = '/html/body/div[2]/div[5]/div/div[3]/div/section/div/div/div/ul/li[1]/div[2]/ul/li[2]/div/div[2]/div/div/div/div/a'
    ASM_2 = '/html/body/div[2]/div[5]/div/div[3]/div/section/div/div/div/ul/li[1]/div[2]/ul/li[3]/div/div[2]/div/div/div/div/a'

    ADD_SUBMISSION_BUTTON = '/html/body/div[2]/div[4]/div/div[2]/div/section/div[2]/div[1]/div/div/div/form/button'

    CLICK_TO_DROP_FILE_BUTTON = '/html/body/div[3]/div[4]/div/div[2]/div/section/div[2]/div/form/fieldset/div[2]/div/div[2]/fieldset/div[1]/div[2]/div[1]/div[1]/div[1]/a'
    CHOOSE_FILE_INPUT = '/html/body/div[6]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div/div/form/div/div[1]/div/input'
    UPLOAD_FILE_BUTTON = '/html/body/div[6]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/button'

    SAVE_CHANGE_BUTTON = '//*[@id="id_submitbutton"]'

    def submit_asm(self, asm, file_path, screenshot_path):
        if asm == 1:
            self.driver.find_element(By.XPATH, self.ASM_1).click()
            time.sleep(5)
        else:
            self.driver.find_element(By.XPATH, self.ASM_2).click()
            time.sleep(5)

        self.driver.find_element(By.XPATH, self.ADD_SUBMISSION_BUTTON).click()
        time.sleep(5)

        self.driver.find_element(By.XPATH, self.CLICK_TO_DROP_FILE_BUTTON).click()
        time.sleep(2)

        self.driver.find_element(By.XPATH, self.CHOOSE_FILE_INPUT).send_keys(os.getcwd() + file_path)
        time.sleep(2)

        self.driver.find_element(By.XPATH, self.UPLOAD_FILE_BUTTON).click()
        time.sleep(30)

        self.driver.find_element(By.XPATH, self.SAVE_CHANGE_BUTTON).click()
        time.sleep(7)

        self.driver.save_screenshot(screenshot_path)
        time.sleep(2)



    def submit_asm_success(self, old_url):
        if self.driver.current_url == old_url + "&action=view":
            print("Result: Submit successfully.")
            return True
        
        print("Result: Fail to submit.")
        return False
    
