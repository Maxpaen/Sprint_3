from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from faker import Faker

class TestRegistration:
    def test_new_user_registration_user_registered(self):
        options = Options()
        options.add_argument('--window-size=1024,768')
        driver = webdriver.Chrome(options=options)
        driver.get("https://stellarburgers.nomoreparties.site/")

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//*[contains(@class, 'button_button_size_large')]")))
        driver.find_element(By.XPATH, ".//*[contains(@class, 'button_button_size_large')]").click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//*[contains(@class, 'Auth_link') and (text()='Зарегистрироваться')]")))
        driver.find_element(By.XPATH, ".//*[contains(@class, 'Auth_link') and (text()='Зарегистрироваться')]").click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//*[contains(@class, 'button_button_size_medium') and (text()='Зарегистрироваться')]")))

        fake = Faker("ru_RU")
        driver.find_element(By.XPATH, ".//label[text()='Имя']/following-sibling::input").send_keys(fake.name())
        driver.find_element(By.XPATH, ".//label[text()='Email']/following-sibling::input").send_keys(fake.ascii_free_email())
        driver.find_element(By.XPATH, ".//label[text()='Пароль']/following-sibling::input").send_keys(fake.password())

        driver.find_element(By.XPATH, ".//*[contains(@class, 'button_button_size_medium') and (text()='Зарегистрироваться')]").click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//*[contains(@class, 'button_button_size_medium') and (text()='Войти')]")))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

        driver.quit()

    def test_new_user_registration_short_password_user_not_registered(self):
        options = Options()
        options.add_argument('--window-size=1024,768')
        driver = webdriver.Chrome(options=options)
        driver.get("https://stellarburgers.nomoreparties.site/")

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, ".//*[contains(@class, 'button_button_size_large')]")))
        driver.find_element(By.XPATH, ".//*[contains(@class, 'button_button_size_large')]").click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, ".//*[contains(@class, 'Auth_link') and (text()='Зарегистрироваться')]")))
        driver.find_element(By.XPATH, ".//*[contains(@class, 'Auth_link') and (text()='Зарегистрироваться')]").click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, ".//*[contains(@class, 'button_button_size_medium') and (text()='Зарегистрироваться')]")))

        fake = Faker("ru_RU")
        driver.find_element(By.XPATH, ".//label[text()='Имя']/following-sibling::input").send_keys(fake.name())
        driver.find_element(By.XPATH, ".//label[text()='Email']/following-sibling::input").send_keys(fake.ascii_free_email())
        driver.find_element(By.XPATH, ".//label[text()='Пароль']/following-sibling::input").send_keys(fake.password(length=5))
        driver.find_element(By.XPATH, ".//*[contains(@class, 'button_button_size_medium') and (text()='Зарегистрироваться')]").click()

        assert driver.find_element(By.XPATH, ".//*[contains(@class, 'input__error') and (text()='Некорректный пароль')]").text == 'Некорректный пароль'

        driver.quit()





