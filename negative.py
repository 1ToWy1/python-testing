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

# Открытие страницы авторизации
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.set_window_size(1920, 1080)

# 1. Ввод неверного логина и пароля
user_name_input = driver.find_element(By.ID, "user-name")
user_name_input.send_keys("invalid_user")

password_input = driver.find_element(By.ID, "password")
password_input.send_keys("wrong_password")

# Нажатие на кнопку входа
login_button = driver.find_element(By.ID, "login-button")
login_button.click()

# 2. Поиск элемента ошибки и проверка его текста
error_message_element = driver.find_element(By.XPATH, "//h3[@data-test='error']")
error_text = error_message_element.text
expected_error = "Epic sadface: Username and password do not match any user in this service"

assert error_text == expected_error, f"Ошибка: Ожидался текст '{expected_error}', но получен '{error_text}'"
print("Текст ошибки корректен:", error_text)

# 3. Нажатие на крестик для закрытия ошибки
close_error_button = driver.find_element(By.CLASS_NAME, "error-button")
close_error_button.click()
print("Сообщение об ошибке успешно закрыто")

driver.quit()