from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from datetime import datetime

# Настройка параметров браузера Chrome
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# Инициализация веб-драйвера
driver = webdriver.Chrome(
    options=options,
    service=ChromeService(ChromeDriverManager().install())
)

# Переход на сайт
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.set_window_size(1920, 1080)

# Поиск и заполнение поля "Логин"
user_name_input = driver.find_element(By.ID, "user-name")
user_name_input.send_keys("standard_user")

# Поиск и заполнение поля "Пароль"
password_input = driver.find_element(By.ID, "password")
password_input.send_keys("secret_sauce")

# Поиск и нажатие на кнопку входа (Login)
login_button = driver.find_element(By.ID, "login-button")
login_button.click()

# Формирование имени файла с датой и временем
now_date = datetime.now().strftime("%Y.%m.%d-%H.%M.%S")
screenshot_name = f"screenshot_{now_date}.png"

# Сохранение скриншота прямо в папку проекта
driver.save_screenshot(screenshot_name)
print(f"Скриншот успешно сохранён: {screenshot_name}")

# Пауза для визуального контроля и закрытие браузера
time.sleep(5)
driver.quit()