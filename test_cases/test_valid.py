import pytest
from selenium.webdriver import Chrome
import pytest
import time

@pytest.fixture(scope = "module")
def set_path():
    global driver
    path = r"C:\driver\chromedriver.exe"
    driver = Chrome(executable_path=path)


def test_valid_text(set_path):

    driver.maximize_window()
    driver.get("https://babynames.com/user/join.php")


def test_reg_url(set_path):

    driver.maximize_window()
    driver.get("https://www.iplt20.com/")


def test_valid_text_box(set_path):

    driver.maximize_window()
    driver.get("https://www.bcci.tv/")



