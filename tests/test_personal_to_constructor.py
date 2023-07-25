from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators as L
from helpers import authorization


class TestConstructor:
    def test_transit_from_personal_area_to_constructor_by_link_successful(self, driver, user_credentials):

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(L.login_button_in_main_page))
        driver.find_element(*L.login_button_in_main_page).click()
        authorization(driver, user_credentials)
        driver.find_element(*L.personal_area_link).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(L.order_history_link))
        driver.find_element(*L.burger_constructor).click()

        assert driver.find_element(*L.create_order_button_in_main_page).text == 'Оформить заказ'

    def test_transit_from_personal_area_to_constructor_by_logo_successful(self, driver, user_credentials):

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(L.login_button_in_main_page))
        driver.find_element(*L.login_button_in_main_page).click()
        authorization(driver, user_credentials)
        driver.find_element(*L.personal_area_link).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(L.order_history_link))
        driver.find_element(*L.logo_burger).click()

        assert driver.find_element(*L.create_order_button_in_main_page).text == 'Оформить заказ'
