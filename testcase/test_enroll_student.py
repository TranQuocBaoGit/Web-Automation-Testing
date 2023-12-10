import pytest
from selenium import webdriver
from pages.my_course import MyCoursePage
from pages.login import LoginPage
from utilities.read_xl import read_data_from_excel, get_testcase_name
from utilities.generate_random_string import generate_random_string
import time

@pytest.mark.usefixtures("set_up")
class TestEnrollStudent:

    FILENAME = "./testdata/data.xlsx"
    SHEET =  "enroll_student"
    driver = None

    @pytest.fixture(scope="session")
    def set_up_session(self, request):
        self.driver = request.config.driver

        self.driver.get("https://school.moodledemo.net/login/index.php")
        self.driver.maximize_window()

        # Login with manager priviledge
        login_page = LoginPage(self.driver)
        login_page.login("teacher", "moodle", "skip")

        self.driver.get("https://school.moodledemo.net/user/index.php?id=69")
        time.sleep(5)

        yield

        self.driver.get("https://school.moodledemo.net/my/courses.php")
        time.sleep(5)
        login_page.logout()

    @pytest.fixture
    def set_up_enroll_student(self, request):
        self.driver = request.config.driver

    @pytest.mark.parametrize("student_name, valid", read_data_from_excel(FILENAME, SHEET), ids=get_testcase_name(FILENAME, SHEET))
    def test_grade_submission(self, set_up_session, set_up_enroll_student, student_name, valid, request):
        my_course_page = MyCoursePage(self.driver)
        screenshot_path = f'./screenshots/enroll_student/{request.node.name}.png'
        my_course_page.enroll_student(student_name, screenshot_path)

        if valid:
            print("\nExpect: Enroll student successfully.")
            print("Result: Enroll student successfully.")
        else:
            print("\nExpect: Enroll zero student.")
            print("Result: Enroll zero student.")