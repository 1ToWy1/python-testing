# Импорт модуля времени для создания пауз между действиями
import time

# Импорт основного класса Selenium для управления веб-браузером
from selenium import webdriver

# Импорт специфичных классов сервисов для управления процессами драйверов
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

# Импорт менеджеров для автоматического скачивания и установки нужных версий драйверов
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

#функция для инициализации и запуска выбранного веб-браузера
def start_browser(name: str) -> webdriver.Remote:

    # Сопоставление имени браузера (в нижнем регистре) с соответствующим драйвером
    match name.lower():
        case "chrome":
            # Инициализация и возврат экземпляра Google Chrome
            return webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install())
            )

        case "firefox":
            # Инициализация и возврат экземпляра Mozilla Firefox
            return webdriver.Firefox(
                service=FirefoxService(GeckoDriverManager().install())
            )

        case "edge":
            # Инициализация и возврат экземпляра Microsoft Edge
            return webdriver.Edge(
                service=EdgeService(EdgeChromiumDriverManager().install())
            )

        case _:
            # Исключение, если переданное имя не совпало ни с одним из вариантов
            raise ValueError(f"Неизвестный браузер: {name}")


# Список браузеров для поочередного тестирования
browsers_list: list[str] = ["chrome", "firefox", "edge"]

# Целевой URL-адрес веб-сайта
url: str = "https://www.saucedemo.com/"

# Поочередный запуск процесса в каждом из браузеров
for browser in browsers_list:
    # 1. Запуск выбранного браузера
    driver: webdriver.Remote = start_browser(browser)

    # 2. Переход на указанный веб-сайт
    driver.get(url)

    # 3. Установка размера окна браузера (Full HD)
    driver.set_window_size(width=1920, height=1080)

    # 4. Временная пауза (3 секунды) для визуальной проверки открытой страницы
    time.sleep(3)

    # 5. Завершение работы текущего браузера и закрытие его окна
    driver.quit()