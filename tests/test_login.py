from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators as L
from helpers import authorization

class TestLogin:
    def test_registered_user_login_login_button_successful(self, driver, user_credentials):

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(L.login_button_in_main_page))
        driver.find_element(*L.login_button_in_main_page).click()
        authorization(driver, user_credentials)

        assert driver.find_element(*L.create_order_button_in_main_page).text == 'Оформить заказ'

    def test_registered_user_login_personal_area_button_successful(self, driver, user_credentials):

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((L.personal_area_link)))
        driver.find_element(*L.personal_area_link).click()
        authorization(driver, user_credentials)

        assert driver.find_element(*L.create_order_button_in_main_page).text == 'Оформить заказ'

    def test_registered_user_login_registration_area_button_successful(self, driver, user_credentials):

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(L.login_button_in_main_page))
        driver.find_element(*L.login_button_in_main_page).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(L.register_link))
        driver.find_element(*L.register_link).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(L.button_login_in_register))
        driver.find_element(*L.button_login_in_register).click()
        authorization(driver, user_credentials)

        assert driver.find_element(*L.create_order_button_in_main_page).text == 'Оформить заказ'

    def test_registered_user_login_forgot_password_area_button_successful(self, driver, user_credentials):

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(L.login_button_in_main_page))
        driver.find_element(*L.login_button_in_main_page).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(L.button_forgot_password))
        driver.find_element(*L.button_forgot_password).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(L.button_login_in_register))
        driver.find_element(*L.button_login_in_register).click()
        authorization(driver, user_credentials)

        assert driver.find_element(*L.create_order_button_in_main_page).text == 'Оформить заказ'
