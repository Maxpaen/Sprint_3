from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators as L
from helpers import authorization

class TestPersonalArea:
    def test_transit_to_personal_area_successful(self, driver, user_credentials):

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(L.login_button_in_main_page))
        driver.find_element(*L.login_button_in_main_page).click()
        authorization(driver, user_credentials)
        driver.find_element(*L.personal_area_link).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(L.order_history_link))

        assert driver.find_element(*L.order_history_link).text == 'История заказов'
