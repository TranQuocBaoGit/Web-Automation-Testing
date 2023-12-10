from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


class MyCoursePage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    NOTIFY_STUDENT_TICKBOX = '//*[@id="page"]/section/div[2]/div[4]/div/div[2]/form/label/input'
    GRADE_FIELD = '//*[@id="id_grade"]'
    FEEDBACK_FRAME = '//*[@id="id_assignfeedbackcomments_editor_ifr"]'
    FEEDBACK_FIELD = '//*[@id="tinymce"]/p'

    SAVE_CHANGE_BUTTON = '//*[@name="savechanges"]'

    ROW_TO_BE_GRADED = '//tr[.//td/div[text()="Submitted for grading"]]'
    GRADE_BUTTON = './/td[6]/a'

    GRADE_PANEL = '//*[@id="page"]/section/div[2]/div[3]'

    GRADE_ERROR_MESSAGE = '//*[@id="id_error_grade"]'
    FEEDBACK_ERROR_MESSAGE = '//*[@id="id_error_assignfeedbackcomments_editor"]'


    def perform_grading(self, grade, feedback, tick, screenshot_path):
        if not tick:
        # Click notify student
            self.driver.find_element(By.XPATH, self.NOTIFY_STUDENT_TICKBOX).click()
            time.sleep(2)

        # Clear grade field
        self.driver.find_element(By.XPATH, self.GRADE_FIELD).clear()
        time.sleep(2)

        # Enter grade
        if grade != None:
            self.driver.find_element(By.XPATH, self.GRADE_FIELD).send_keys(grade)
            time.sleep(2)

        # Find feedback frame
        feeback_frame = self.driver.find_element(By.XPATH, self.FEEDBACK_FRAME)
        self.driver.switch_to.frame(feeback_frame)
        time.sleep(2)

        # Clear feedback field
        self.driver.find_element(By.XPATH, self.FEEDBACK_FIELD).clear()
        time.sleep(2)

        if feedback != None:
            # Enter feedback
            self.driver.find_element(By.XPATH, self.FEEDBACK_FIELD).send_keys(feedback)
            time.sleep(2)

        # Switch back to default frame
        self.driver.switch_to.default_content()
        time.sleep(2)

        # Click save change
        self.driver.find_element(By.XPATH, self.SAVE_CHANGE_BUTTON).click()
        time.sleep(5)

        # Get grade panel
        grade_panel = self.driver.find_element(By.XPATH, self.GRADE_PANEL)
        time.sleep(2)

        self.driver.execute_script("arguments[0].scrollBy(0, 400);", grade_panel)
        time.sleep(2)

        # Take screenshot
        grade_panel.screenshot(screenshot_path)
        time.sleep(2)





    def get_submit_to_grade(self):
        row_to_be_graded = self.driver.find_element(By.XPATH, self.ROW_TO_BE_GRADED)
        row_to_be_graded.find_element(By.XPATH, self.GRADE_BUTTON).click()
        time.sleep(10)

        actions = ActionChains(self.driver)
        actions.move_by_offset(50, 200).click().perform()
        time.sleep(2)

        self.driver.refresh()
        time.sleep(10)


    def grade_success(self):
        # Return error message if login fail by checking if URL change
        grade_error = self.driver.find_element(By.XPATH, self.GRADE_ERROR_MESSAGE).text
        if grade_error != "":
            print(f"Result: {grade_error}")
            return grade_error
        
        feedback_error = self.driver.find_element(By.XPATH, self.FEEDBACK_ERROR_MESSAGE).text
        if feedback_error != "":
            print(f"Result: {feedback_error}")
            return feedback_error
        
        print("Result: Successfully graded.")
        
        return "Successfully graded."
    


    ENROLL_USER_BUTTON = '/html/body/div[2]/div[5]/div/div[3]/div/section/div/div[1]/div/div[2]/div/div/form/div/input[1]'
    USER_FIELD = '/html/body/div[7]/div[2]/div/div/div[2]/form/fieldset/div[2]/div[1]/div[2]/div[3]/input'
    USER_CHOICE = '/html/body/div[7]/div[2]/div/div/div[2]/form/fieldset/div[2]/div[1]/div[2]/ul/li/span/span[1]'

    CONFIRM_ENROLL_USER_BUTTON = '/html/body/div[4]/div[2]/div/div/div[3]/button[2]'


    def enroll_student(self, student_name, screenshot_path):

        # Click enroll user
        self.driver.find_element(By.XPATH, self.ENROLL_USER_BUTTON).click()

        # Enter user name
        self.driver.find_element(By.XPATH, self.USER_FIELD).send_keys(student_name)
        time.sleep(5)

        self.choose_user()
        time.sleep(5)

        # Click enroll button
        self.driver.find_element(By.XPATH, self.CONFIRM_ENROLL_USER_BUTTON).click()
        time.sleep(2)

        # Take screenshot
        self.driver.save_screenshot(screenshot_path)
        time.sleep(2)


    def choose_user(self):
        try:
            # Choose first user
            self.driver.find_element(By.XPATH, self.USER_CHOICE).click()
            time.sleep(2)
        except:
            pass

