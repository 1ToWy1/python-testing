from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time

# Настройка параметров браузера Chrome
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# Инициализация драйвера
driver = webdriver.Chrome(
    options=options,
    service=ChromeService(ChromeDriverManager().install())
)

# Переход на сайт
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.set_window_size(1920, 1080)

# 1. Авторизация на сайте
user_name_input = driver.find_element(By.ID, "user-name")
user_name_input.send_keys("standard_user")

password_input = driver.find_element(By.ID, "password")
password_input.send_keys("secret_sauce")

login_button = driver.find_element(By.ID, "login-button")
login_button.click()

# 2. Добавление всех товаров в корзину
# Находим все кнопки "Add to cart" на странице и кликаем по каждой из них
add_to_cart_buttons = driver.find_elements(By.XPATH, "//button[contains(@text, 'Add to cart') or contains(@id, 'add-to-cart')]")
for button in add_to_cart_buttons:
    button.click()

# 3. Переход в корзину
shopping_cart_link = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
shopping_cart_link.click()

# 4. Поиск последнего товара в корзине и скролл к нему через move_to_element
cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
last_cart_item = cart_items[-1]  # Берем последний элемент из списка

# Инициализируем ActionChains и перемещаем курсор/скроллим к последнему элементу
action = ActionChains(driver)
action.move_to_element(last_cart_item).perform()

print("Страница успешно проскроллена до последнего элемента в корзине")

# Задержка для визуальной проверки результата
time.sleep(5)

# Закрытие браузера и завершение сессии
driver.quit()