from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class CourseSettingPage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    AVAILABILITY_SECTION = '//*[@id="id_availability"]'

    FROM_DATE_SELECT = '//*[@id="id_allowsubmissionsfromdate_day"]'
    FROM_MONTH_SELECT = '//*[@id="id_allowsubmissionsfromdate_month"]'
    FROM_YEAR_SELECT = '//*[@id="id_allowsubmissionsfromdate_year"]'

    DUE_DATE_SELECT = '//*[@id="id_duedate_day"]'
    DUE_MONTH_SELECT = '//*[@id="id_duedate_month"]'
    DUE_YEAR_SELECT = '//*[@id="id_duedate_year"]'

    DUE_ERROR= '//*[@id="id_error_duedate"]'

    SAVE_AND_DISPLAY_BUTTON = '//*[@id="id_submitbutton"]'

    def set_availability(self, from_date, from_month, from_year, due_date, due_month, due_year, screenshot_path):

        availability_section = self.driver.find_element(By.XPATH, self.AVAILABILITY_SECTION)
        self.driver.execute_script("arguments[0].scrollIntoView();", availability_section)

        # Select from date
        self.select_drop_down(self.FROM_DATE_SELECT, from_date)

        # Select from month
        self.select_drop_down(self.FROM_MONTH_SELECT, from_month)

        # Select from year
        self.select_drop_down(self.FROM_YEAR_SELECT, from_year)

        # Select due date
        self.select_drop_down(self.DUE_DATE_SELECT, due_date)

        # Select due month
        self.select_drop_down(self.DUE_MONTH_SELECT, due_month)

        # Select due year
        self.select_drop_down(self.DUE_YEAR_SELECT, due_year)

        # Save and return to course
        self.driver.find_element(By.XPATH, self.SAVE_AND_DISPLAY_BUTTON).click()
        time.sleep(5)

        # Screenshot
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.DUE_ERROR)))
            self.driver.execute_script("arguments[0].scrollIntoView();", availability_section)
            self.driver.execute_script("window.scrollTo(0, -100);")
            time.sleep(2)
            availability_section.screenshot(screenshot_path)
        except:
            self.driver.save_screenshot(screenshot_path)


    def select_drop_down(self, object_path, value):
        object = self.driver.find_element(By.XPATH, object_path)
        time.sleep(2)
        object_option = Select(object)
        object_option.select_by_visible_text(value)
        time.sleep(2)


    def set_due_date_success(self):
        # Check if the error message present
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.DUE_ERROR)))
            due_error_message = self.driver.find_element(By.XPATH, self.DUE_ERROR).text
            print(f"Result: {due_error_message}")
            return False
        except:
            print("Result: Set due day successfully.")
            return True
        
