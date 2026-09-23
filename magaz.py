import time
from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# --- НАСТРОЙКИ И ИНИЦИАЛИЗАЦИЯ ---

fake = Faker()

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(
    options=options,
    service=ChromeService(ChromeDriverManager().install())
)

wait = WebDriverWait(driver, 10)

base_url = 'https://www.saucedemo.com/'
driver.get(base_url)

# Авторизация
username_input = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
username_input.send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
wait.until(EC.url_contains("/inventory.html"))

# ---ПРИВЕТСТВИЕ И ВАЛИДАЦИЯ ВЫБОРА ТОВАРА---

print("Приветствую тебя в нашем интернет - магазине")
print("Выбери один из следующих товаров и укажи его номер: "
      "1 - Sauce Labs Backpack, "
      "2 - Sauce Labs Bike Light, "
      "3 - Sauce Labs Bolt T-Shirt, "
      "4 - Sauce Labs Fleece Jacket, "
      "5 - Sauce Labs Onesie, "
      "6 - Test.allTheThings() T-Shirt (Red)")

products = {
    "1": "Sauce Labs Backpack",
    "2": "Sauce Labs Bike Light",
    "3": "Sauce Labs Bolt T-Shirt",
    "4": "Sauce Labs Fleece Jacket",
    "5": "Sauce Labs Onesie",
    "6": "Test.allTheThings() T-Shirt (Red)"
}

user_choice = None
while user_choice not in products:
    raw_input = input("\nВведите номер товара (1-6): ").strip()
    if raw_input in products:
        user_choice = raw_input
    else:
        print(f" Неверный ввод '{raw_input}'. Пожалуйста, выберите цифру от 1 до 6.")

selected_product = products[user_choice]
print(f"\n Выбран товар: {selected_product}")

# ---ДОБАВЛЕНИЕ В КОРЗИНУ И СОХРАНЕНИЕ ЦЕНЫ---

product_card = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, f"//div[contains(@class, 'inventory_item') and .//div[text()='{selected_product}']]")
    )
)

original_price = product_card.find_element(By.CLASS_NAME, "inventory_item_price").text.replace("$", "").strip()
print(f" Цена на витрине: ${original_price}")

add_btn = product_card.find_element(By.CLASS_NAME, "btn_primary")
add_btn.click()

wait.until(
    EC.text_to_be_present_in_element(
        (By.XPATH, f"//div[contains(@class, 'inventory_item') and .//div[text()='{selected_product}']]//button"),
        "Remove"
    )
)

driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

# ---ОФОРМЛЕНИЕ ЗАКАЗА С ГЕНЕРАЦИЕЙ ДАННЫХ---

wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

first_name = fake.first_name()
last_name = fake.last_name()
zip_code = fake.zipcode()

print(f"\n Данные покупателя: {first_name} {last_name}, ZIP: {zip_code}")

driver.find_element(By.ID, "first-name").send_keys(first_name)
driver.find_element(By.ID, "last-name").send_keys(last_name)
driver.find_element(By.ID, "postal-code").send_keys(zip_code)
driver.find_element(By.ID, "continue").click()

# ---ПРОВЕРКА ТОВАРА НА СТРАНИЦЕ OVERVIEW (ИСПРАВЛЕНО)---

# ИСПРАВЛЕНИЕ: используем правильный класс cart_item вместо несуществующего summary_item
order_item = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, f"//div[contains(@class, 'cart_item') and contains(., '{selected_product}')]")
    )
)

# Проверка названия (используем contains, т.к. текст может быть разбит переносами)
actual_name_el = order_item.find_element(By.CLASS_NAME, "inventory_item_name")
actual_name = actual_name_el.text.strip()
assert selected_product in actual_name, (
    f"Ошибка имени! Ожидалось '{selected_product}', получено '{actual_name}'"
)
print(f" Название совпадает: {actual_name}")

# Проверка цены
actual_price = order_item.find_element(By.CLASS_NAME, "inventory_item_price").text.replace("$", "").strip()
assert actual_price == original_price, (
    f"Ошибка цены! Ожидалось '${original_price}', получено '${actual_price}'"
)
print(f" Цена совпадает: ${actual_price}")

# ---ЗАВЕРШЕНИЕ ЗАКАЗА---

driver.find_element(By.ID, "finish").click()

success_msg = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "complete-header")))
assert "Thank you for your order!" in success_msg.text, "Заказ не оформлен!"
print(" Заказ успешно оформлен!")

driver.quit()