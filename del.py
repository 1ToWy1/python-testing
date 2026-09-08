from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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

# 1. Первоначальный ввод некорректных данных
user_name_input = driver.find_element(By.ID, "user-name")
user_name_input.send_keys("invalid_user")

password_input = driver.find_element(By.ID, "password")
password_input.send_keys("invalid_password")

time.sleep(1)  # Задержка для визуального контроля введенных неверных данных

# 2. Выделение и удаление текста в поле "Логин"
user_name_input.send_keys(Keys.CONTROL + "a")  # Выделить весь текст
user_name_input.send_keys(Keys.BACKSPACE)      # Удалить выделенный текст

# 3. Выделение и удаление текста в поле "Пароль"
password_input.send_keys(Keys.CONTROL + "a")   # Выделить весь текст
password_input.send_keys(Keys.DELETE)         # Удалить выделенный текст

time.sleep(1)

# 4. Ввод корректных значений логина и пароля
user_name_input.send_keys("standard_user")
password_input.send_keys("secret_sauce")

# 5. Поиск и нажатие на кнопку входа (Login)
login_button = driver.find_element(By.ID, "login-button")
login_button.click()

# Пауза для визуального контроля результата
time.sleep(5)

# Закрытие браузера и завершение сессии
driver.quit()