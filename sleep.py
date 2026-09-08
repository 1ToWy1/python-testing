import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
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

# Ввод неверного логина и пароля
user_name_input = driver.find_element(By.ID, "user-name")
user_name_input.send_keys("invalid_user")

password_input = driver.find_element(By.ID, "password")
password_input.send_keys("wrong_password")

# Нажатие на кнопку входа
login_button = driver.find_element(By.ID, "login-button")
login_button.click()

# Проверка текста ошибки
error_message_element = driver.find_element(By.XPATH, "//h3[@data-test='error']")
error_text = error_message_element.text
expected_error = "Epic sadface: Username and password do not match any user in this service"

assert error_text == expected_error, f"Ошибка: Ожидался текст '{expected_error}', но получен '{error_text}'"
print("Текст ошибки корректен:", error_text)

# Закрытие сообщения об ошибке
close_error_button = driver.find_element(By.CLASS_NAME, "error-button")
close_error_button.click()
print("Сообщение об ошибке закрыто")

# Задержка перед обновлением (3 секунды)
time.sleep(3)

# Обновление страницы
driver.refresh()
print("Запрос на обновление страницы отправлен")

# Проверка перезагрузки: находим поле заново и проверяем, что атрибут value пуст
user_name_input_after_refresh = driver.find_element(By.ID, "user-name")
user_name_value = user_name_input_after_refresh.get_attribute("value")

assert user_name_value == "", f"Ошибка: страница не обновилась, поле логина содержит значение '{user_name_value}'"
print("Проверка пройдена: страница обновилась, поля ввода очистились")

# Задержка после обновления для визуального контроля (5 секунд)
time.sleep(5)

# Закрытие браузера и завершение сессии
driver.quit()
