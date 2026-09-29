from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from login_page import LoginPage


class SauceDemoTest:
    # Локаторы элементов страницы
    INVENTORY_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "btn_primary")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self) -> None:
        # Настройка браузера и явного ожидания
        options = Options()
        options.add_argument("--start-maximized")

        self.driver: webdriver.Chrome = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )

        self.wait: WebDriverWait = WebDriverWait(self.driver, 10)
        self.base_url: str = "https://www.saucedemo.com/"

    def open_site(self) -> None:
        """Открывает главную страницу сайта."""
        print("Открываем сайт...")
        self.driver.get(self.base_url)

    def authorize(self, username: str, password: str) -> None:
        """Выполняет авторизацию пользователя."""
        print("Выполняем авторизацию...")

        login_page = LoginPage(self.driver, self.wait)
        login_page.login(username, password)

        self.wait.until(EC.url_contains("/inventory.html"))

        print("Авторизация прошла успешно!")

    def select_first_product(self) -> str:
        """Добавляет первый товар в корзину."""
        print("Выбираем первый товар...")

        first_product_name: str = self.wait.until(
            EC.element_to_be_clickable(self.INVENTORY_ITEM_NAME)
        ).text

        add_to_cart_btn = self.wait.until(
            EC.element_to_be_clickable(self.ADD_TO_CART_BUTTON)
        )
        add_to_cart_btn.click()

        print(f"Товар '{first_product_name}' добавлен в корзину.")

        return first_product_name

    def go_to_cart(self) -> None:
        """Переходит в корзину."""
        print("Переходим в корзину...")

        cart_link = self.wait.until(
            EC.element_to_be_clickable(self.CART_LINK)
        )
        cart_link.click()

    def verify_cart_page(self) -> None:
        """Проверяет, что открыта страница корзины."""
        print("Проверяем страницу корзины...")

        self.wait.until(EC.url_contains("/cart.html"))

        current_url: str = self.driver.current_url

        assert "/cart.html" in current_url, (
            f"Ошибка! Мы не в корзине. Текущий URL: {current_url}"
        )

        print(f"Успешно в корзине! URL: {current_url}")

        self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        )

        print("Кнопка Checkout доступна.")

    def run_full_test(self) -> None:
        """Запускает полный сценарий теста."""
        self.open_site()
        self.authorize("standard_user", "secret_sauce")

        product_name: str = self.select_first_product()

        self.go_to_cart()
        self.verify_cart_page()

        print(f"Товар в корзине: {product_name}")


if __name__ == "__main__":
    test_runner = SauceDemoTest()

    try:
        test_runner.run_full_test()
    finally:
        # Закрываем браузер даже при ошибке теста
        test_runner.driver.quit()
        print("Браузер закрыт.")
