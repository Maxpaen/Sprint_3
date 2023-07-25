from selenium.webdriver.common.by import By

class Locators:
    login_email = By.XPATH, ".//label[text()='Email']/following-sibling::input"  #Ввод Email для входа и регистрации
    login_password = By.XPATH, ".//label[text()='Пароль']/following-sibling::input"  #Ввод пароля при регистрации
    register_name = By.XPATH, ".//label[text()='Имя']/following-sibling::input"  # Ввод имени при регистрации
    password = By.XPATH, ".//input[@type=\'password\' and @name=\'Пароль\']"  # Ввод пароля для входа
    login_button = By.XPATH, ".//button[text()='Войти']"  # Кнопка "Войти" авторизации
    register_link = By.XPATH, ".//*[contains(@class, 'Auth_link') and (text()='Зарегистрироваться')]" #Кнопка с переходом на страницу регистрации
    register_button = By.XPATH, "//button[text()='Зарегистрироваться']"  # Кнопка регистрации
    text_error_register = By.XPATH, "//p[text()='Некорректный пароль']"  # Ошибка "Некорректный пароль" при регистрации
    login_button_in_main_page = By.XPATH, ".//button[text() = 'Войти в аккаунт']"  # Кнопка "Войти в Аккаунт" на главной странице
    create_order_button_in_main_page = By.XPATH, ".//button[text() = 'Оформить заказ']" # Кнопка "Оформить заказ" на главной странице
    burger_constructor = By.XPATH, "//p[contains(text(),'Конструктор')]/parent::a"  # Кнопа "Конструктор"
    constructor_h1_text = By.XPATH, "// h1[text()='Соберите бургер']"
    acc_button = By.XPATH, "//a[@href = '/account']"  # Кнопка "Личный кабинет"
    button_login_in_register = By.XPATH, "//a[@href = '/login']"  # Кнопка "Войти" на странице регистрации
    button_forgot_password = By.XPATH, "//a[@href = '/forgot-password']"  # Кнопка "Восстановить пароль"
    logo_burger = By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']"  # Логотип "Stellar Burgers"
    logout_button = By.XPATH, ".//button[text() = 'Выход']" # кнопка "Выйти"
    sauces_section = By.XPATH, '//span[contains(text(),"Соусы")]'  # Фильтр Соусы
    buns_section = By.XPATH, '//span[contains(text(),"Булки")]'  # Фильтр Булки
    stuffing_section = By.XPATH, '//span[contains(text(),"Начинки")]'  # Фильтр Начинки
    stuffing = By.XPATH, ".//*[contains(@class, 'tab_tab__1SPyG')][3]" # Начинки
    sauces = By.XPATH, ".//*[contains(@class, 'tab_tab__1SPyG')][2]" # Соусы
    buns = By.XPATH, ".//*[contains(@class, 'tab_tab__1SPyG')][1]" # Булки
    login_title = (By.XPATH, "//h2[text()='Вход']")
    personal_area_link = By.XPATH, ".//*[contains(@class, 'AppHeader_header') and (text()='Личный Кабинет')]" # Кнопка для перехода в "Личный кабинет"
    order_history_link = By.XPATH, ".//*[contains(@class, 'text_type_main-medium') and (text()='История заказов')]" # Кнопка для перехода в "История заказов"