from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

class TestLogin:
    def test_registered_user_login_login_button_successful(self, user_credentials):
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
        assert driver.find_element(By.XPATH, ".//*[contains(@class, 'button_button_size_large') and (text()='Оформить заказ')]").text == 'Оформить заказ'

        driver.quit()

    def test_registered_user_login_personal_area_button_successful(self, user_credentials):
        options = Options()
        options.add_argument('--window-size=1024,768')
        driver = webdriver.Chrome(options=options)
        driver.get("https://stellarburgers.nomoreparties.site/")

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//*[contains(@class, 'AppHeader_header') and (text()='Личный Кабинет')]")))
        driver.find_element(By.XPATH, ".//*[contains(@class, 'button_button_size_large')]").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//*[contains(@class, 'AppHeader_header') and (text()='Личный Кабинет')]")))
        driver.find_element(By.XPATH, ".//label[text()='Email']/following-sibling::input").send_keys(user_credentials.get('login'))
        driver.find_element(By.XPATH, ".//label[text()='Пароль']/following-sibling::input").send_keys(user_credentials.get('password'))
        driver.find_element(By.XPATH, ".//*[contains(@class, 'button_button_size_medium') and (text()='Войти')]").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//*[contains(@class, 'button_button_size_large') and (text()='Оформить заказ')]")))
        assert driver.find_element(By.XPATH, ".//*[contains(@class, 'button_button_size_large') and (text()='Оформить заказ')]").text == 'Оформить заказ'

        driver.quit()

    def test_registered_user_login_registration_area_button_successful(self, user_credentials):
        options = Options()
        options.add_argument('--window-size=1024,768')
        driver = webdriver.Chrome(options=options)
        driver.get("https://stellarburgers.nomoreparties.site/")

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//*[contains(@class, 'button_button_size_large')]")))
        driver.find_element(By.XPATH, ".//*[contains(@class, 'button_button_size_large')]").click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//*[contains(@class, 'Auth_link') and (text()='Зарегистрироваться')]")))
        driver.find_element(By.XPATH, ".//*[contains(@class, 'Auth_link') and (text()='Зарегистрироваться')]").click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//*[contains(@class, 'Auth_link') and (text()='Войти')]")))
        driver.find_element(By.XPATH, ".//*[contains(@class, 'Auth_link') and (text()='Войти')]").click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//label[text()='Email']/following-sibling::input")))
        driver.find_element(By.XPATH, ".//label[text()='Email']/following-sibling::input").send_keys(user_credentials.get('login'))
        driver.find_element(By.XPATH, ".//label[text()='Пароль']/following-sibling::input").send_keys(user_credentials.get('password'))
        driver.find_element(By.XPATH, ".//*[contains(@class, 'button_button_size_medium') and (text()='Войти')]").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//*[contains(@class, 'button_button_size_large') and (text()='Оформить заказ')]")))
        assert driver.find_element(By.XPATH, ".//*[contains(@class, 'button_button_size_large') and (text()='Оформить заказ')]").text == 'Оформить заказ'

        driver.quit()

    def test_registered_user_login_forgot_password_area_button_successful(self, user_credentials):
        options = Options()
        options.add_argument('--window-size=1024,768')
        driver = webdriver.Chrome(options=options)
        driver.get("https://stellarburgers.nomoreparties.site/")

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//*[contains(@class, 'button_button_size_large')]")))
        driver.find_element(By.XPATH, ".//*[contains(@class, 'button_button_size_large')]").click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//*[contains(@class, 'Auth_link') and (text()='Восстановить пароль')]")))
        driver.find_element(By.XPATH, ".//*[contains(@class, 'Auth_link') and (text()='Восстановить пароль')]").click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//*[contains(@class, 'Auth_link') and (text()='Войти')]")))
        driver.find_element(By.XPATH, ".//*[contains(@class, 'Auth_link') and (text()='Войти')]").click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//label[text()='Email']/following-sibling::input")))
        driver.find_element(By.XPATH, ".//label[text()='Email']/following-sibling::input").send_keys(user_credentials.get('login'))
        driver.find_element(By.XPATH, ".//label[text()='Пароль']/following-sibling::input").send_keys(user_credentials.get('password'))
        driver.find_element(By.XPATH, ".//*[contains(@class, 'button_button_size_medium') and (text()='Войти')]").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//*[contains(@class, 'button_button_size_large') and (text()='Оформить заказ')]")))
        assert driver.find_element(By.XPATH, ".//*[contains(@class, 'button_button_size_large') and (text()='Оформить заказ')]").text == 'Оформить заказ'

        driver.quit()
