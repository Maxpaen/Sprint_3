from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators as L

def authorization(driver, user_credentials):
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(L.login_email))
    driver.find_element(*L.login_email).send_keys(user_credentials.get('login'))
    driver.find_element(*L.login_password).send_keys(user_credentials.get('password'))
    driver.find_element(*L.login_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(L.create_order_button_in_main_page))