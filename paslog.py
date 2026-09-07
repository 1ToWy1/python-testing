from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Настройка параметров браузера Chrome
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # Чтобы браузер не закрывался автоматически после выполнения

# Инициализация веб-драйвера
driver = webdriver.Chrome(
    options=options,
    service=ChromeService(ChromeDriverManager().install())
)

# Переход на сайт
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)

# Настройка размера окна браузера
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

# Пауза для визуального контроля результата
time.sleep(5)

# Закрытие браузера и завершение сессии
driver.quit()