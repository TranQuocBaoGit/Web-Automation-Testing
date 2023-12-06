import pytest
from selenium import webdriver
from pages.login import LoginPage
from utilities.read_xl import read_data_from_excel

@pytest.mark.usefixtures("set_up")
class TestLogin:
    @pytest.fixture(autouse=True)
    def set_up_login(self):
        self.driver.get("https://school.moodledemo.net/login/index.php")
        self.driver.maximize_window()
        yield
        if self.driver.current_url == "https://school.moodledemo.net/my/courses.php":
            login_page = LoginPage(self.driver)
            login_page.logout()

    @pytest.mark.parametrize("username, password, valid", read_data_from_excel("./testdata/data.xlsx", "login"))
    def test_login(self, username, password, valid):
        login_page = LoginPage(self.driver)
        login_page.login(username, password)
        assert login_page.login_success() == valid
