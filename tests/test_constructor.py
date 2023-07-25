from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators as L
from helpers import authorization

class TestLogin:
    def test_sauce_section_switches_on(self, driver, user_credentials):

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(L.login_button_in_main_page))
        driver.find_element(*L.login_button_in_main_page).click()
        authorization(driver, user_credentials)
        driver.find_element(*L.sauces_section).click()
        assert 'current' in driver.find_element(*L.sauces).get_attribute("class")

    def test_stuffing_section_switches_on(self, driver, user_credentials):

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(L.login_button_in_main_page))
        driver.find_element(*L.login_button_in_main_page).click()
        authorization(driver, user_credentials)
        driver.find_element(*L.stuffing_section).click()
        assert 'current' in driver.find_element(*L.stuffing).get_attribute("class")

    def test_bun_section_switches_on(self, driver, user_credentials):

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(L.login_button_in_main_page))
        driver.find_element(*L.login_button_in_main_page).click()
        authorization(driver, user_credentials)
        driver.find_element(*L.stuffing_section).click()
        driver.find_element(*L.buns_section).click()
        assert 'current' in driver.find_element(*L.buns).get_attribute("class")
