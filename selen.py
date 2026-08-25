"""
Модуль для автоматического запуска браузера Chrome и перехода
на тестовый веб-сайт SauceDemo.
"""

# Импорт основного модуля Selenium для управления браузером
from selenium import webdriver

# Импорт класса Service для работы с драйвером Chrome
from selenium.webdriver.chrome.service import Service as ChromeService

# Импорт менеджера драйверов для автоматической установки/обновления chromedriver
from webdriver_manager.chrome import ChromeDriverManager


def open_saucedemo_page() -> webdriver.Chrome:
    """
    Инициализирует веб-драйвер Chrome, настраивает параметры запуска,
    открывает целевой URL и устанавливает размер окна.

    :return: Экземпляр веб-драйвера Chrome (webdriver.Chrome)
    """
    # 1. Настройка параметров (опций) браузера Chrome
    options: webdriver.ChromeOptions = webdriver.ChromeOptions()

    # Опция "detach" оставляет браузер открытым после завершения работы скрипта
    options.add_experimental_option("detach", True)

    # 2. Инициализация сервиса драйвера с помощью ChromeDriverManager
    # Менеджер автоматически скачивает нужную версию ChromeDriver под текущий Chrome
    service: ChromeService = ChromeService(ChromeDriverManager().install())

    # 3. Запуск экземпляра браузера Chrome с переданными опциями и сервисом
    driver: webdriver.Chrome = webdriver.Chrome(service=service, options=options)

    # 4. Определение целевого URL-адреса
    base_url: str = "https://www.saucedemo.com/"

    # 5. Переход по указанной ссылке
    driver.get(base_url)

    # 6. Установка разрешения окна браузера (Full HD)
    driver.set_window_size(width=1920, height=1080)

    # Возвращаем объект драйвера для дальнейшей работы с элементами страницы
    return driver


# Точка входа в скрипт
if __name__ == "__main__":
    # Вызов функции для открытия страницы
    web_driver: webdriver.Chrome = open_saucedemo_page()
    print("Страница SauceDemo успешно открыта.")
