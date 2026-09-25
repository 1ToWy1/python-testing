# Импортируем необходимые библиотеки и модули
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class SauceDemoTest:
    def __init__(self) -> None:
        # Настраиваем опции Chrome (например, можно добавить headless режим)
        options: Options = Options()
        options.add_argument("--start-maximized")

        # Инициализируем драйвер с автоматической установкой chromedriver
        self.driver: webdriver.Chrome = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )
        print("Браузер успешно запущен")

    def open_site(self, url: str) -> None:

        print(f" Переход на сайт: {url}")
        self.driver.get(url)

    def close_browser(self) -> None:

        if self.driver:
            self.driver.quit()
            print("Браузер закрыт")


# --- Основная логика запуска ---
if __name__ == "__main__":
    # Создаем экземпляр класса (автоматически запустится браузер)
    test_instance: SauceDemoTest = SauceDemoTest()

    try:
        # Вызываем метод класса для перехода на сайт
        test_instance.open_site("https://www.saucedemo.com/")

        print("Тест успешно выполнен!")

    finally:
        # Гарантированно закрываем браузер даже при возникновении ошибок
        test_instance.close_browser()
