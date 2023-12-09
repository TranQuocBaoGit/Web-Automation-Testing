import pytest
from selenium import webdriver
from pages.course_setting import CourseSettingPage
from pages.login import LoginPage
from utilities.read_xl import read_data_from_excel, get_testcase_name
import time

@pytest.mark.usefixtures("set_up")
class TestAsmDueDate:

    FILENAME = "./testdata/data.xlsx"
    SHEET =  "asm_due_date"
    driver = None

    @pytest.fixture(scope="session")
    def set_up_session(self, request):
        self.driver = request.config.driver

        self.driver.get("https://school.moodledemo.net/login/index.php")
        self.driver.maximize_window()

        # Login with manager priviledge
        login_page = LoginPage(self.driver)
        login_page.login("teacher", "moodle", "skip")

        yield

        self.driver.get("https://school.moodledemo.net/my/courses.php")
        time.sleep(5)
        login_page.logout()

    @pytest.fixture
    def set_up_due_date(self, request):
        self.driver = request.config.driver
        self.driver.get("https://school.moodledemo.net/course/modedit.php?update=980&return=1")
        time.sleep(5)

    @pytest.mark.parametrize("from_date, from_month, from_year, due_date, due_month, due_year, valid", read_data_from_excel(FILENAME, SHEET), ids=get_testcase_name(FILENAME, SHEET))
    def test_asm_due_date(self, set_up_session, set_up_due_date, from_date, from_month, from_year, due_date, due_month, due_year, valid, request):
        course_setting = CourseSettingPage(self.driver)
        screenshot_path = f'./screenshots/asm_due_date/{request.node.name}.png'
        course_setting.set_availability(str(int(from_date)), str(from_month), str(int(from_year)), str(int(due_date)), str(due_month), str(int(due_year)), screenshot_path)

        if valid:
            print("\nExpect: Set due day successfully.")
        else:
            print("\nExpect: Due date must be after the allow submissions from date.")
        assert course_setting.set_due_date_success() == valid