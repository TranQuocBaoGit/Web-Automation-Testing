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



    CREATE_COURSE_BUTTON = '//*[@id="linkcourses"]/div/div[1]/div[2]/ul/li[3]/a'

    COURSE_FULL_NAME_INPUT = '//*[@id="id_fullname"]'
    COURSE_SHORT_NAME_INPUT = '//*[@id="id_shortname"]'
    COURSE_CATEGORY_DROPDOWN = '/html/body/div[3]/div[3]/div/div[3]/div/section/div/form/fieldset[1]/div[2]/div[3]/div[2]/div[3]/span'

    COURSE_CATEGORY_CHOICE = '/html/body/div[3]/div[3]/div/div[3]/div/section/div/form/fieldset[1]/div[2]/div[3]/div[2]/ul'
    DELETE_COURSE_CATEGORY = '/html/body/div[3]/div[3]/div/div[3]/div/section/div/form/fieldset[1]/div[2]/div[3]/div[2]/div[2]/span'

    SAVE_AND_DISPLAY_COURSE_BUTTON = '//*[@id="id_saveanddisplay"]'

    FULL_NAME_ERROR = '//*[@id="id_error_fullname"]'
    SHORT_NAME_ERROR = '//*[@id="id_error_shortname"]'
    CATEGORY_ERROR = '//*[@id="id_error_category"]'


    def create_course(self,  course_full_name, course_short_name, course_category, screenshot_path):
        # Click create course
        self.driver.find_element(By.XPATH, self.CREATE_COURSE_BUTTON).click()
        time.sleep(5)

        if course_full_name != None:
            # Enter full course name
            self.driver.find_element(By.XPATH, self.COURSE_FULL_NAME_INPUT).send_keys(course_full_name)
            time.sleep(2)

        if course_short_name != None:
            # Enter short course name
            self.driver.find_element(By.XPATH, self.COURSE_SHORT_NAME_INPUT).send_keys(course_short_name)
            time.sleep(2)

        if course_category != None:
            # Click category dropdown
            self.driver.find_element(By.XPATH, self.COURSE_CATEGORY_DROPDOWN).click()
            time.sleep(2)

            # Find all the choice
            course_category_choice = self.driver.find_element(By.XPATH, self.COURSE_CATEGORY_CHOICE)
            time.sleep(2)

            # Click choice
            choice_path = f'//li[contains(text(), "{course_category}")]'
            course_category_choice.find_element(By.XPATH, choice_path).click()
            time.sleep(2)
        else:
            # Delete default course category
            self.driver.find_element(By.XPATH, self.DELETE_COURSE_CATEGORY).click()
            time.sleep(2)

        # Save and wait for load
        self.driver.find_element(By.XPATH, self.SAVE_AND_DISPLAY_COURSE_BUTTON).click()
        time.sleep(10)

        # Save screenshot
        self.driver.save_screenshot(screenshot_path)
        time.sleep(2)


    def create_course_success(self):
        # Return error message if create user fail by checking if URL change
        if "https://school.moodledemo.net/course/edit.php" not in self.driver.current_url:
            print("Result: Create new course successfully.")
        else:
            print("Result: Fail to create new course.")
        return ("https://school.moodledemo.net/course/edit.php" not in self.driver.current_url)