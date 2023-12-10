import pytest
from selenium import webdriver
from pages.admin_site import AdminSitePage
from pages.login import LoginPage
from utilities.read_xl import read_data_from_excel, get_testcase_name
import time

@pytest.mark.usefixtures("set_up")
class TestCreateCourse:

    FILENAME = "./testdata/data.xlsx"
    SHEET =  "create_course"
    driver = None

    @pytest.fixture(scope="session")
    def set_up_session(self, request):
        self.driver = request.config.driver

        self.driver.get("https://school.moodledemo.net/login/index.php")
        self.driver.maximize_window()

        # Login with manager priviledge
        login_page = LoginPage(self.driver)
        login_page.login("manager", "moodle", "skip")

        yield

        self.driver.get("https://school.moodledemo.net/my/courses.php")
        login_page.logout()

    @pytest.fixture
    def set_up_create_course(self, request):
        self.driver = request.config.driver

        self.driver.get("https://school.moodledemo.net/admin/search.php#linkcourses")
        time.sleep(5)

        yield
        time.sleep(5)

    @pytest.mark.parametrize("course_full_name, course_short_name, course_category, valid", read_data_from_excel(FILENAME, SHEET), ids=get_testcase_name(FILENAME, SHEET))
    def test_create_course(self, set_up_session, set_up_create_course, course_full_name, course_short_name, course_category, valid, request):
        admin_page = AdminSitePage(self.driver)

        screenshot_path = f'./screenshots/create_course/{request.node.name}.png'
        admin_page.create_course(course_full_name, course_short_name, course_category, screenshot_path)

        if valid:
            print("\nExpect: Create new course successfully.")
        else:
            print("\nExpect: Fail to create new course.")
        assert admin_page.create_course_success() == valid