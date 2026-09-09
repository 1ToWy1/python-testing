import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# настройка параметров браузера chrome
options = webdriver.ChromeOptions()

# открытие браузера сразу во весь экран
options.add_argument("--start-maximized")

# отключение политики проверки утечки паролей и сохраненных паролей chrome
prefs = {
    "profile.password_manager_leak_detection": False,
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
}
options.add_experimental_option("prefs", prefs)
options.add_experimental_option("detach", True)

# инициализация веб-драйвера
driver = webdriver.Chrome(
    options=options,
    service=ChromeService(ChromeDriverManager().install())
)

# вызов разворачивания окна на весь экран
driver.maximize_window()

# переход на сайт
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)

# авторизация на сайте
user_name_input = driver.find_element(By.ID, "user-name")
user_name_input.send_keys("standard_user")

password_input = driver.find_element(By.ID, "password")
password_input.send_keys("secret_sauce")

login_button = driver.find_element(By.ID, "login-button")
login_button.click()
print("Успешная авторизация")

time.sleep(2)

# выбор товара и добавление в корзину
add_to_cart_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
add_to_cart_button.click()
print("Товар добавлен в корзину")

time.sleep(1)

# переход в корзину
shopping_cart_link = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
shopping_cart_link.click()
print("Перешли на страницу корзины")

assert "cart.html" in driver.current_url, "Ошибка: не удалось перейти в корзину"

time.sleep(2)

# возврат на страницу каталога с помощью back()
driver.back()
print("Вернулись назад на страницу каталога")

assert "inventory.html" in driver.current_url, "Ошибка: не удалось вернуться на страницу каталога"

time.sleep(2)

# переход обратно в корзину с помощью forward()
driver.forward()
print("Перешли вперед обратно на страницу корзины")

assert "cart.html" in driver.current_url, "Ошибка: не удалось вернуться в корзину через forward()"

time.sleep(3)

# закрытие браузера и завершение сессии
driver.quit()