import pytest
from selenium import webdriver
from pages.profile import ProfilePage
from pages.login import LoginPage
from utilities.read_xl import read_data_from_excel, get_testcase_name
import time

@pytest.mark.usefixtures("set_up")
class TestEditProfile:

    FILENAME = "./testdata/data.xlsx"
    SHEET =  "edit_profile"
    driver = None
    
    @pytest.fixture(scope="session")
    def set_up_session(self, request):
        self.driver = request.config.driver

        self.driver.get("https://school.moodledemo.net/login/index.php")
        self.driver.maximize_window()

        # Login with manager priviledge
        login_page = LoginPage(self.driver)
        login_page.login("student", "moodle", "skip")

        yield

        self.driver.get("https://school.moodledemo.net/my/courses.php")
        login_page.logout()

    @pytest.fixture
    def set_up_edit_profile(self, request):
        self.driver = request.config.driver

        self.driver.get("https://school.moodledemo.net/user/profile.php")
        time.sleep(5)

        yield
        time.sleep(5)

    @pytest.mark.parametrize("first_name, last_name, email, valid", read_data_from_excel(FILENAME, SHEET), ids=get_testcase_name(FILENAME, SHEET))
    def test_edit_profile(self, set_up_session, set_up_edit_profile, first_name, last_name, email, valid, request):
        profile_page = ProfilePage(self.driver)

        screenshot_path = f'./screenshots/edit_profile/{request.node.name}.png'
        profile_page.edit_profile(first_name, last_name, email, screenshot_path)

        if valid:
            print("\nExpect: Edit profile successfully.")
        else:
            print("\nExpect: Edit profile fail.")
        assert profile_page.edit_profile_success() == valid