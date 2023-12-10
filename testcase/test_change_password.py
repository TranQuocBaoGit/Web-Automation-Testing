import pytest
from selenium import webdriver
from pages.preferences import PreferencePage
from pages.login import LoginPage
from utilities.read_xl import read_data_from_excel, get_testcase_name
import time

@pytest.mark.usefixtures("set_up")
class TestChangePassword:

    FILENAME = "./testdata/data.xlsx"
    SHEET =  "change_password"
    driver = None

    result = ["Change password successfully.", 
              "Missing field.", 
              "Invalid login, please try again.", 
              "The new password must be different than the current one.", 
              "These passwords do not match."]
    
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
    def set_up_change_password(self, request):
        self.driver = request.config.driver

        if self.driver.current_url != 'https://school.moodledemo.net/user/preferences.php':
            self.driver.get("https://school.moodledemo.net/user/preferences.php")
        time.sleep(5)

        yield
        time.sleep(5)

    @pytest.mark.parametrize("current_password, new_password, repeat_new_password, valid", read_data_from_excel(FILENAME, SHEET), ids=get_testcase_name(FILENAME, SHEET))
    def test_change_password(self, set_up_session, set_up_change_password, current_password, new_password, repeat_new_password, valid, request):
        preference_page = PreferencePage(self.driver)

        screenshot_path = f'./screenshots/change_password/{request.node.name}.png'
        preference_page.change_password(current_password, new_password, repeat_new_password, screenshot_path)

        valid = int(valid)

        print(f"\nExpect: {self.result[valid]}")
        assert preference_page.change_password_success() == self.result[valid]