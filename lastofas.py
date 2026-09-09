from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Настройка параметров браузера Chrome
options = webdriver.ChromeOptions()

# 1. Отключение менеджмента и проверки утечки паролей (PasswordLeakDetectionEnabled = False)
prefs = {
    "profile.password_manager_leak_detection": False,  # Отключает проверку утечки паролей
    "credentials_enable_service": False,               # Отключает всплывающее окно сохранения паролей
    "profile.password_manager_enabled": False          # Отключает встроенный менеджер паролей
}
options.add_experimental_option("prefs", prefs)

# Чтобы браузер не закрывался автоматически после выполнения
options.add_experimental_option("detach", True)

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

# 2. Авторизация на сайте
user_name_input = driver.find_element(By.ID, "user-name")
user_name_input.send_keys("standard_user")

password_input = driver.find_element(By.ID, "password")
password_input.send_keys("secret_sauce")

login_button = driver.find_element(By.ID, "login-button")
login_button.click()

# Небольшая пауза для завершения загрузки страницы
time.sleep(2)

# 3. Открытие скрытого бокового меню (бургер-меню)
burger_menu_button = driver.find_element(By.ID, "react-burger-menu-btn")
burger_menu_button.click()
print("Скрытое меню успешно открыто")

# Пауза для завершения анимации открытия меню
time.sleep(1)

# 4. Нажатие на кнопку выхода (Logout)
logout_link = driver.find_element(By.ID, "logout_sidebar_link")
logout_link.click()
print("Нажата кнопка Logout")

# Пауза для завершения редиректа на страницу входа
time.sleep(2)

# 5. Проверка разлогина путем сравнения текущего URL с базовым
current_url = driver.current_url
assert current_url == base_url, f"Ошибка: Ожидался URL '{base_url}', но получен '{current_url}'"
print(f"Проверка успешна: пользователь разлогинен, текущий URL: {current_url}")

# Пауза для визуального контроля результата
time.sleep(3)

# Закрытие браузера и завершение сессии
driver.quit()
