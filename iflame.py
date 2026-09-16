from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Настройка Chrome
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

# Запуск браузера
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

# Явное ожидание
wait = WebDriverWait(driver, 10)

# Переход на страницу
base_url = "https://www.lambdatest.com/selenium-playground/iframe-demo/"
driver.get(base_url)

# Находим iframe с редактором и переключаемся внутрь него
iframe = wait.until(EC.presence_of_element_located((By.ID, "iFrame1")))
driver.switch_to.frame(iframe)

# Находим поле редактора
input_pole = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".rsw-ce")))

# Запоминаем исходный текст
text_value = "LambdaTest Selenium"

# Удаляем старый текст и вводим свой
input_pole.click()
input_pole.send_keys(Keys.CONTROL, "a")
input_pole.send_keys(text_value)

# Запоминаем текст до изменения начертания
value_before = input_pole.text
print("Текст до форматирования:", value_before)

# Выделяем введённый текст
input_pole.send_keys(Keys.CONTROL, "a")

# Нажимаем кнопку Bold для изменения начертания текста
bold_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@title='Bold']")))
bold_button.click()

# Получаем текст после изменения начертания
value_after = input_pole.text
print("Текст после форматирования:", value_after)

# Проверяем, что текст не изменился
assert value_before == value_after, f"Текст изменился: было '{value_before}', стало '{value_after}'"

print("Текст не изменился, форматирование применено")

time.sleep(3)