from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from faker import Faker
from locators import Locators as L

class TestRegistration:
    def test_new_user_registration_user_registered(self, driver):

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(L.login_button_in_main_page))
        driver.find_element(*L.login_button_in_main_page).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(L.register_link))
        driver.find_element(*L.register_link).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(L.register_button))

        fake = Faker("ru_RU")
        driver.find_element(*L.register_name).send_keys(fake.name())
        driver.find_element(*L.login_email).send_keys(fake.ascii_free_email())
        driver.find_element(*L.login_password).send_keys(fake.password())
        driver.find_element(*L.register_button).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(L.login_button))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    def test_new_user_registration_short_password_user_not_registered(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(L.login_button_in_main_page))
        driver.find_element(*L.login_button_in_main_page).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(L.register_link))
        driver.find_element(*L.register_link).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(L.register_button))

        fake = Faker("ru_RU")
        driver.find_element(*L.register_name).send_keys(fake.name())
        driver.find_element(*L.login_email).send_keys(fake.ascii_free_email())
        driver.find_element(*L.login_password).send_keys(fake.password(length=5))
        driver.find_element(*L.register_button).click()

        assert driver.find_element(*L.text_error_register).text == 'Некорректный пароль'
