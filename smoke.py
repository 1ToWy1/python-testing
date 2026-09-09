import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Настройка параметров браузера Chrome
options = webdriver.ChromeOptions()

prefs = {
    "profile.password_manager_leak_detection": False,
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
}
options.add_experimental_option("prefs", prefs)
options.add_experimental_option("detach", True)  # Чтобы браузер не закрывался автоматически

# Инициализация драйвера
driver = webdriver.Chrome(
    options=options,
    service=ChromeService(ChromeDriverManager().install())
)

# Переход на сайт
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.set_window_size(1920, 1080)

# Авторизация
user_name_input = driver.find_element(By.ID, "user-name")
user_name_input.send_keys("standard_user")

password_input = driver.find_element(By.ID, "password")
password_input.send_keys("secret_sauce")

login_button = driver.find_element(By.ID, "login-button")
login_button.click()
print("Успешная авторизация")

# Выбор и сохранение 2 товаров
# Товар 1: Sauce Labs Backpack
product_1_title = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']/div")
value_product_1 = product_1_title.text

product_1_price = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']/ancestor::div[@class='inventory_item_description']//div[@class='inventory_item_price']")
value_price_product_1 = product_1_price.text

add_to_cart_button_1 = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
add_to_cart_button_1.click()

# Товар 2: Sauce Labs Bike Light
product_2_title = driver.find_element(By.XPATH, "//a[@id='item_0_title_link']/div")
value_product_2 = product_2_title.text

product_2_price = driver.find_element(By.XPATH, "//a[@id='item_0_title_link']/ancestor::div[@class='inventory_item_description']//div[@class='inventory_item_price']")
value_price_product_2 = product_2_price.text

add_to_cart_button_2 = driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
add_to_cart_button_2.click()

print(f"Товар 1: {value_product_1} — {value_price_product_1}")
print(f"Товар 2: {value_product_2} — {value_price_product_2}")

# Корзина и оформление
shopping_cart_link = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
shopping_cart_link.click()

checkout_button = driver.find_element(By.ID, "checkout")
checkout_button.click()

# Заполнение данных покупателя
first_name_input = driver.find_element(By.ID, "first-name")
first_name_input.send_keys("Ivan")

last_name_input = driver.find_element(By.ID, "last-name")
last_name_input.send_keys("Ivanov")

postal_code_input = driver.find_element(By.ID, "postal-code")
postal_code_input.send_keys("16798")
print("Данные покупателя заполнены")

button_continue = driver.find_element(By.ID, "continue")
button_continue.click()

# Проверка

# Проверка первого товара (Название и Цена)
finish_product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']/div")
value_finish_product_1 = finish_product_1.text
assert value_product_1 == value_finish_product_1, f"Ошибка в названии 1-го товара: {value_product_1} != {value_finish_product_1}"
print("Info Finish Product 1 good")

finish_price_product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']/ancestor::div[@class='cart_item']//div[@class='inventory_item_price']")
value_finish_price_product_1 = finish_price_product_1.text
assert value_price_product_1 == value_finish_price_product_1, f"Ошибка в цене 1-го товара: {value_price_product_1} != {value_finish_price_product_1}"
print("Info Finish Price Product 1 good")

# Проверка второго товара (Название и Цена)
finish_product_2 = driver.find_element(By.XPATH, "//a[@id='item_0_title_link']/div")
value_finish_product_2 = finish_product_2.text
assert value_product_2 == value_finish_product_2, f"Ошибка в названии 2-го товара: {value_product_2} != {value_finish_product_2}"
print("Info Finish Product 2 good")

finish_price_product_2 = driver.find_element(By.XPATH, "//a[@id='item_0_title_link']/ancestor::div[@class='cart_item']//div[@class='inventory_item_price']")
value_finish_price_product_2 = finish_price_product_2.text
assert value_price_product_2 == value_finish_price_product_2, f"Ошибка в цене 2-го товара: {value_price_product_2} != {value_finish_price_product_2}"
print("Info Finish Price Product 2 good")

# Проверка суммы.
# Получаем фактическую итоговую строку суммы
summary_price = driver.find_element(By.CLASS_NAME, "summary_subtotal_label")
value_summary_price = summary_price.text
print(f"Отображаемый итог на сайте: {value_summary_price}")

# Переводим сохраненные ценники из формата "$29.99" в числа float (29.99) и складываем
price_1_num = float(value_finish_price_product_1.replace("$", ""))
price_2_num = float(value_finish_price_product_2.replace("$", ""))
calculated_sum = price_1_num + price_2_num

# Формируем ожидаемую строку в формате системы Sauce Demo
expected_item_total = f"Item total: ${calculated_sum:.2f}"
print(f"Расчитанный итог: {expected_item_total}")

# Сверяем сумму
assert value_summary_price == expected_item_total, f"Ошибка! Расчет не совпал: {value_summary_price} != {expected_item_total}"
print("Total Summary Price good")

# Завершаем покупку
button_finish = driver.find_element(By.ID, "finish")
button_finish.click()
print("Enter Button Finish")

# Проверка успешного завершения заказа
checkout_complete = driver.find_element(By.CLASS_NAME, "complete-header")
value_checkout_complete = checkout_complete.text
print(value_checkout_complete)

assert value_checkout_complete == "Thank you for your order!", f"Ошибка: Заказ не оформлен. Текст: '{value_checkout_complete}'"
print("Info Order Complete")

# Пауза и закрытие браузера
time.sleep(3)
driver.quit()