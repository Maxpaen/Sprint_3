import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from data import url


@pytest.fixture
def user_credentials():
    user_credentials = {'login': 'abayushkin_11@ya.ru', 'password': 'Bentley1'}
    return user_credentials

@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--window-size=1024,768')
    driver = webdriver.Chrome(options=options)
    driver.get(url.main)

    yield driver
    driver.quit()