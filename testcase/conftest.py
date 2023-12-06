import pytest
from selenium import webdriver

# Function in this file act as a config for other testcase


@pytest.fixture(scope="class") # This specify the function will be ran in the scope of class
def set_up(request):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver
    yield
    driver.close()
