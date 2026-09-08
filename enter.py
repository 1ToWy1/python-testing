import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# Настройка параметров браузера Chrome
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # Оставлять браузер открытым

# Инициализация драйвера
driver = webdriver.Chrome(
    options=options,
    service=ChromeService(ChromeDriverManager().install())
)

# Переход на сайт
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.set_window_size(1920, 1080)

# 1. Поиск полей и ввод первичных данных
user_name_input = driver.find_element(By.ID, "user-name")
user_name_input.send_keys("invalid_user")

password_input = driver.find_element(By.ID, "password")
password_input.send_keys("wrong_password")

time.sleep(2)  # Пауза для визуальной проверки введенного текста

# 2. Выделение и удаление текста в поле "Логин" (Ctrl + A -> Backspace)
user_name_input.send_keys(Keys.CONTROL + "a")
user_name_input.send_keys(Keys.BACKSPACE)

# 3. Выделение и удаление текста в поле "Пароль" (Ctrl + A -> Delete)
password_input.send_keys(Keys.CONTROL + "a")
password_input.send_keys(Keys.DELETE)

time.sleep(1)

# 4. Нажатие на кнопку авторизации с помощью клавиши ENTER
# Нажимаем Enter, находясь в поле пароля (или логина)
password_input.send_keys(Keys.ENTER)

# 5. Проверка появления ошибки о пустом поле логина
error_message = driver.find_element(By.XPATH, "//h3[@data-test='error']").text
expected_error = "Epic sadface: Username is required"

assert error_message == expected_error, f"Ошибка: Ожидался текст '{expected_error}', но получен '{error_message}'"
print("Тест пройден: отправили форму через ENTER, получена ошибка 'Username is required'")

# Задержка и завершение сессии
time.sleep(3)
driver.quit()