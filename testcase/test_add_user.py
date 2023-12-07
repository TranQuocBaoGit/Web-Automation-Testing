import pytest
from selenium import webdriver
from pages.admin_site import AdminSitePage
from pages.login import LoginPage
from utilities.read_xl import read_data_from_excel, get_testcase_name
import time

@pytest.mark.usefixtures("set_up")
class TestAddUser:

    FILENAME = "./testdata/data.xlsx"
    SHEET =  "add_user"
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
    def set_up_add_user(self, request):
        self.driver = request.config.driver

        self.driver.get("https://school.moodledemo.net/admin/search.php#linkusers")
        time.sleep(5)

        yield
        
        self.driver.get("https://school.moodledemo.net/admin/search.php#linkusers")
        time.sleep(5)

    @pytest.mark.parametrize("username, new_password, fname, lname, email, valid", read_data_from_excel(FILENAME, SHEET), ids=get_testcase_name(FILENAME, SHEET))
    def test_add_user(self, set_up_session, set_up_add_user, username, new_password, fname, lname, email, valid, request):
        admin_page = AdminSitePage(self.driver)

        screenshot_path = f'./screenshots/add_user/{request.node.name}.png'
        admin_page.add_user(username, new_password, fname, lname, email, screenshot_path)

        if valid:
            print("\nExpect: Create new user successfully")
        else:
            print("\nExpect: Fail to create new user")
        assert admin_page.create_user_success() == valid