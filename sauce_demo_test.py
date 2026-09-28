from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Импорт класса авторизации из отдельного файла
from login_page import LoginPage


class SauceDemoTest:
    # Локаторы элементов, используемых в тесте
    INVENTORY_ITEM_NAME: tuple = (By.CLASS_NAME, "inventory_item_name")

    ADD_TO_CART_BUTTON: tuple = (By.CLASS_NAME, "btn_primary")

    CART_LINK: tuple = (By.CLASS_NAME, "shopping_cart_link")

    CHECKOUT_BUTTON: tuple = (By.ID, "checkout")

    def __init__(self) -> None:

        # Настройка опций Chrome
        options: Options = Options()

        options.add_argument("--start-maximized")

        # Создание экземпляра драйвера через webdriver_manager
        self.driver: webdriver.Chrome = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options,
        )

        # Глобальное явное ожидание (10 секунд)
        self.wait: WebDriverWait = WebDriverWait(self.driver, 10)

        # Базовый URL тестируемого сайта
        self.base_url: str = "https://www.saucedemo.com/"

    def open_site(self) -> None:

        print("Открываем сайт...")

        self.driver.get(self.base_url)

    def authorize(self, username: str, password: str) -> None:

        print("Выполняем авторизацию...")

        login_page = LoginPage(self.driver, self.wait)

        login_page.login(username, password)

        # Проверяем успешный вход по URL
        self.wait.until(EC.url_contains("/inventory.html"))

        print("Авторизация прошла успешно!")

    def select_first_product(self) -> str:

        print("Выбираем первый товар...")

        # Ожидаем кликабельности названия первого товара
        first_product_name = self.wait.until(
            EC.element_to_be_clickable(self.INVENTORY_ITEM_NAME)
        ).text

        # Ожидаем кликабельности кнопки "Add to cart" и нажимаем
        add_to_cart_btn = self.wait.until(
            EC.element_to_be_clickable(self.ADD_TO_CART_BUTTON)
        )

        add_to_cart_btn.click()

        print(f"Товар '{first_product_name}' добавлен в корзину.")

        return first_product_name

    def go_to_cart(self) -> None:

        print("Переходим в корзину...")

        cart_link = self.wait.until(
            EC.element_to_be_clickable(self.CART_LINK)
        )

        cart_link.click()

    def verify_cart_page(self) -> None:

        # Ожидание кликабельности кнопки Checkout
        self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        )

        current_url: str = self.driver.current_url

        assert "/cart.html" in current_url, (
            f"Ошибка! Мы не в корзине. Текущий URL: {current_url}"
        )

        print(f"Успешно в корзине! URL: {current_url}")

    def run_full_test(self) -> None:

        try:
            self.open_site()

            self.authorize("standard_user", "secret_sauce")

            product_name = self.select_first_product()

            self.go_to_cart()

            self.verify_cart_page()

            print(f"Товар в корзине: {product_name}")

        finally:
            # Гарантированное закрытие браузера
            self.driver.quit()

            print("Браузер закрыт.")


if __name__ == "__main__":
    test_runner = SauceDemoTest()

    test_runner.run_full_test()
