from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestPersonalArea:
    def test_logged_in_user_logout_successful(self, driver, user_credentials):

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//*[contains(@class, 'button_button_size_large')]")))
        driver.find_element(By.XPATH, ".//*[contains(@class, 'button_button_size_large')]").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//label[text()='Email']/following-sibling::input")))
        driver.find_element(By.XPATH, ".//label[text()='Email']/following-sibling::input").send_keys(user_credentials.get('login'))
        driver.find_element(By.XPATH, ".//label[text()='Пароль']/following-sibling::input").send_keys(user_credentials.get('password'))
        driver.find_element(By.XPATH, ".//*[contains(@class, 'button_button_size_medium') and (text()='Войти')]").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//*[contains(@class, 'button_button_size_large') and (text()='Оформить заказ')]")))
        driver.find_element(By.XPATH, ".//*[contains(@class, 'AppHeader_header') and (text()='Личный Кабинет')]").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//*[contains(@class, 'text_type_main-medium') and (text()='История заказов')]")))
        driver.find_element(By.XPATH, ".//*[contains(@class, 'Account_button') and (text()='Выход')]").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//*[contains(@class, 'button_button_size_medium') and (text()='Войти')]")))

        assert driver.find_element(By.XPATH, ".//*[contains(@class, 'button_button_size_medium') and (text()='Войти')]").text == 'Войти'
