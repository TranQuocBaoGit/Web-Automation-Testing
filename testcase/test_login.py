import pytest
from selenium import webdriver
from pages.login import LoginPage
from utilities.read_xl import read_data_from_excel, get_testcase_name

@pytest.mark.usefixtures("set_up")
class TestLogin:

    FILENAME = "./testdata/data.xlsx"
    SHEET =  "login"

    @pytest.fixture(autouse=True)
    def set_up_login(self, request):
        self.driver = request.config.driver

        self.driver.get("https://school.moodledemo.net/login/index.php")
        self.driver.maximize_window()

        yield

        if self.driver.current_url == "https://school.moodledemo.net/my/courses.php":
            login_page = LoginPage(self.driver)
            login_page.logout()

    @pytest.mark.parametrize("username, password, valid", read_data_from_excel(FILENAME, SHEET), ids=get_testcase_name(FILENAME, SHEET))
    def test_login(self, username, password, valid, request):
        login_page = LoginPage(self.driver)

        screenshot_path = f'screenshots/login/{request.node.name}.png'
        login_page.login(username, password, screenshot_path)

        if valid:
            print("\nExpect: Login successfully")
        else:
            print("\nExpect: Fail to login")
        assert login_page.login_success() == valid
