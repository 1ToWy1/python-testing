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

# Проверяем соответствие URL
print(driver.current_url)
get_url = driver.current_url
url = 'https://www.saucedemo.com/inventory.html'
assert url == get_url
print('Корректный URL')

#Проверяем что находимся на странице каталога
text_products = driver.find_element(By.XPATH, "//span[@class='title']")
print(text_products.text)
value_text_products = text_products.text
assert value_text_products == 'Products'
print('Корректный заголовок')

# Пауза для визуального контроля результата
time.sleep(5)

# Закрытие браузера и завершение сессии
driver.quit()