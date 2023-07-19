from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

class TestConstructor:
    def test_transit_from_personal_area_to_constructor_by_link_successful(self, user_credentials):
        options = Options()
        options.add_argument('--window-size=1024,768')
        driver = webdriver.Chrome(options=options)
        driver.get("https://stellarburgers.nomoreparties.site/")

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//*[contains(@class, 'button_button_size_large')]")))
        driver.find_element(By.XPATH, ".//*[contains(@class, 'button_button_size_large')]").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//label[text()='Email']/following-sibling::input")))
        driver.find_element(By.XPATH, ".//label[text()='Email']/following-sibling::input").send_keys(user_credentials.get('login'))
        driver.find_element(By.XPATH, ".//label[text()='Пароль']/following-sibling::input").send_keys(user_credentials.get('password'))
        driver.find_element(By.XPATH, ".//*[contains(@class, 'button_button_size_medium') and (text()='Войти')]").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//*[contains(@class, 'button_button_size_large') and (text()='Оформить заказ')]")))
        driver.find_element(By.XPATH, ".//*[contains(@class, 'AppHeader_header') and (text()='Личный Кабинет')]").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//*[contains(@class, 'text_type_main-medium') and (text()='История заказов')]")))
        driver.find_element(By.XPATH, ".//*[contains(@class, 'AppHeader_header') and (text()='Конструктор')]").click()

        assert driver.find_element(By.XPATH, ".//*[contains(@class, 'button_button_size_large') and (text()='Оформить заказ')]").text == 'Оформить заказ'

        driver.quit()

    def test_transit_from_personal_area_to_constructor_by_logo_successful(self, user_credentials):
        options = Options()
        options.add_argument('--window-size=1024,768')
        driver = webdriver.Chrome(options=options)
        driver.get("https://stellarburgers.nomoreparties.site/")

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//*[contains(@class, 'button_button_size_large')]")))
        driver.find_element(By.XPATH, ".//*[contains(@class, 'button_button_size_large')]").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//label[text()='Email']/following-sibling::input")))
        driver.find_element(By.XPATH, ".//label[text()='Email']/following-sibling::input").send_keys(user_credentials.get('login'))
        driver.find_element(By.XPATH, ".//label[text()='Пароль']/following-sibling::input").send_keys(user_credentials.get('password'))
        driver.find_element(By.XPATH, ".//*[contains(@class, 'button_button_size_medium') and (text()='Войти')]").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//*[contains(@class, 'button_button_size_large') and (text()='Оформить заказ')]")))
        driver.find_element(By.XPATH, ".//*[contains(@class, 'AppHeader_header') and (text()='Личный Кабинет')]").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//*[contains(@class, 'text_type_main-medium') and (text()='История заказов')]")))
        driver.find_element(By.XPATH, "//*[contains(@class, 'AppHeader_header__logo')]").click()

        assert driver.find_element(By.XPATH, ".//*[contains(@class, 'button_button_size_large') and (text()='Оформить заказ')]").text == 'Оформить заказ'

        driver.quit()