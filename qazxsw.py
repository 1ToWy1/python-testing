from faker import Faker

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Создаём объект Faker
fake = Faker()

# Настройка Chrome
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

# Запуск браузера
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

# Явное ожидание
wait = WebDriverWait(driver, 10)

# Переход на страницу SauceDemo
driver.get("https://www.saucedemo.com/")

# Генерируем случайное имя пользователя
random_username = fake.user_name()

# Находим поле Username
username_input = wait.until(EC.element_to_be_clickable((By.ID, "user-name")))

# Вводим сгенерированное имя пользователя
username_input.send_keys(random_username)

# Проверяем, что имя пользователя введено
assert username_input.get_attribute("value") == random_username, "Имя пользователя введено неправильно"

print("Сгенерированное имя пользователя:", random_username)

driver.quit()
