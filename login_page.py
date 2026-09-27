from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:


    # Локаторы элементов страницы логина
    USERNAME_INPUT: tuple = (By.ID, "user-name")
    PASSWORD_INPUT: tuple = (By.ID, "password")
    LOGIN_BUTTON: tuple = (By.ID, "login-button")

    def __init__(self, driver, wait: WebDriverWait) -> None:

        self.driver = driver
        self.wait = wait

    def login(self, username: str, password: str) -> None:
        
        # Ожидаем кликабельности поля логина
        username_field = self.wait.until(
            EC.element_to_be_clickable(self.USERNAME_INPUT)
        )
        username_field.clear()
        username_field.send_keys(username)

        # Ожидаем кликабельности поля пароля
        password_field = self.wait.until(
            EC.element_to_be_clickable(self.PASSWORD_INPUT)
        )
        password_field.clear()
        password_field.send_keys(password)

        # Ожидаем кликабельности кнопки Login и нажимаем
        login_btn = self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        )
        login_btn.click()
