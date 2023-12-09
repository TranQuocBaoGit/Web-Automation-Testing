import pytest
from selenium import webdriver
from pages.my_course import MyCoursePage
from pages.login import LoginPage
from utilities.read_xl import read_data_from_excel, get_testcase_name
from utilities.generate_random_string import generate_random_string
import time

@pytest.mark.usefixtures("set_up")
class TestGradeSubmission:

    FILENAME = "./testdata/data.xlsx"
    SHEET =  "grade_submission"
    driver = None

    result = ["Successfully graded.", 
              "Grade must be less than or equal to 100.", 
              "The grade provided could not be understood: ", 
              "Feedback is too long.", 
              "Grade must be greater than or equal to zero."]

    @pytest.fixture(scope="session")
    def set_up_session(self, request):
        self.driver = request.config.driver

        self.driver.get("https://school.moodledemo.net/login/index.php")
        self.driver.maximize_window()

        # Login with manager priviledge
        login_page = LoginPage(self.driver)
        login_page.login("teacher", "moodle", "skip")

        self.driver.get("https://school.moodledemo.net/mod/assign/view.php?id=980&action=grading")
        time.sleep(5)

        my_course_page = MyCoursePage(self.driver)
        my_course_page.get_submit_to_grade()

        yield

        self.driver.get("https://school.moodledemo.net/my/courses.php")
        time.sleep(5)
        login_page.logout()

    @pytest.fixture
    def set_up_grade_submission(self, request):
        self.driver = request.config.driver

    @pytest.mark.parametrize("grade, feedback_length, tick, valid", read_data_from_excel(FILENAME, SHEET), ids=get_testcase_name(FILENAME, SHEET))
    def test_grade_submission(self, set_up_session, set_up_grade_submission, grade, feedback_length, tick, valid, request):
        feedback = generate_random_string(feedback_length)

        my_course_page = MyCoursePage(self.driver)
        screenshot_path = f'./screenshots/grade_submission/{request.node.name}.png'
        my_course_page.perform_grading(grade, feedback, tick, screenshot_path)
        
        valid = int(valid)

        expect_result = f"{self.result[valid]}" + (grade if valid == 2 else "")
        print(f"\nExpect: {self.result[valid]}" + (grade if valid == 2 else ""))
        assert my_course_page.grade_success() == expect_result