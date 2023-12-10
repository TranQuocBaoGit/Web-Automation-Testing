import pytest
from selenium import webdriver
from pages.asm import AsmPage
from pages.login import LoginPage
from utilities.read_xl import read_data_from_excel, get_testcase_name
import time

@pytest.mark.usefixtures("set_up")
class TestSubmitAsm:

    FILENAME = "./testdata/data.xlsx"
    SHEET =  "submit_asm"
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
    def set_up_submit_asm(self, request):
        self.driver = request.config.driver

        self.driver.get("https://school.moodledemo.net/course/view.php?id=51")
        time.sleep(5)

        yield
        time.sleep(5)

    @pytest.mark.parametrize("asm, file_path, valid", read_data_from_excel(FILENAME, SHEET), ids=get_testcase_name(FILENAME, SHEET))
    def test_submit_asm_and_upload_file(self, set_up_session, set_up_submit_asm, asm, file_path, valid, request):
        asm_page = AsmPage(self.driver)

        if file_path == 1:
            file_path = "/file1.png"
        elif file_path == 2:
            file_path = "/file2.jpg"
        else:
            file_path = "/file3.pdf"

        screenshot_path = f'./screenshots/submit_asm/{request.node.name}.png'
        asm_page.submit_asm(asm, file_path, screenshot_path)

        if valid:
            print("\nExpect: Submit successfully.")
            print("Result: Submit successfully.")
        else:
            print("\nExpect: Fail to submit.")
            print("Result: Fail to submit.")
        assert asm_page.submit_asm_success() == valid