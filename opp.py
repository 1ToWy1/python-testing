from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class SauceDemoTest:

    def __init__(self) -> None:

        options: Options = Options()
        options.add_argument("--start-maximized")

        self.driver: webdriver.Chrome = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )
        # Глобальное ожидание для всех элементов (10 секунд)
        self.wait: WebDriverWait = WebDriverWait(self.driver, 10)
        self.base_url: str = "https://www.saucedemo.com/"

    def run_full_test(self) -> None:

        try:
            # Шаг 1: Открытие сайта
            print(" Открываем сайт...")
            self.driver.get(self.base_url)

            # Шаг 2: Ввод логина и пароля
            print(" Выполняем авторизацию...")
            username_field = self.wait.until(
                EC.visibility_of_element_located((By.ID, "user-name"))
            )
            username_field.send_keys("standard_user")

            password_field = self.driver.find_element(By.ID, "password")
            password_field.send_keys("secret_sauce")

            # Шаг 3: Нажатие кнопки Логин
            login_btn = self.driver.find_element(By.ID, "login-button")
            login_btn.click()

            # Проверка успешного входа по изменению URL
            self.wait.until(EC.url_contains("/inventory.html"))
            print(" Авторизация прошла успешно!")

            # Шаг 4: Выбираем продукт из каталога (первый попавшийся для примера)
            print(" Выбираем первый товар...")
            first_product_name = self.wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name"))
            ).text

            add_to_cart_btn = self.driver.find_element(By.CLASS_NAME, "btn_primary")
            add_to_cart_btn.click()
            print(f" Товар '{first_product_name}' добавлен в корзину.")

            # Шаг 5: Переходим в корзину
            print(" Переходим в корзину...")
            cart_link = self.driver.find_element(By.CLASS_NAME, "shopping_cart_link")
            cart_link.click()

            # Шаг 6: Проверяем, что находимся в корзине.
            # Ждем, пока кнопка CHECKOUT OUT станет кликабельной — это подтверждает загрузку страницы
            checkout_btn = self.wait.until(
                EC.element_to_be_clickable((By.ID, "checkout"))
            )

            current_url = self.driver.current_url
            assert "/cart.html" in current_url, f"Ошибка! Мы не в корзине. Текущий URL: {current_url}"

            print(f" Успешно в корзине! URL: {current_url}")
            print(f" Товар в корзине: {first_product_name}")

        except Exception as e:
            print(f" Ошибка при выполнении теста: {e}")
        finally:
            # Гарантированное закрытие браузера после завершения
            self.driver.quit()
            print(" Браузер закрыт.")


# --- Основная точка входа ---
if __name__ == "__main__":
    # Создаем экземпляр класса
    test_runner: SauceDemoTest = SauceDemoTest()

    # Вызываем метод класса для запуска всех шагов
    test_runner.run_full_test()
