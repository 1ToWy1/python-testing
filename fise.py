from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
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
driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")

# Значение для блока Single Input Field
message_value = "Hello Selenium"

# Находим поле для ввода сообщения
message_input = wait.until(EC.element_to_be_clickable((By.ID, "user-message")))
message_input.send_keys(message_value)

# Нажимаем кнопку Get Checked Value
show_button = wait.until(EC.element_to_be_clickable((By.ID, "showInput")))
show_button.click()

# Получаем отображённое сообщение
message_result = wait.until(EC.visibility_of_element_located((By.ID, "message")))

# Сравниваем введённое и полученное значение
assert message_result.text == message_value, f"Ожидалось {message_value}, получено {message_result.text}"

print("Значения равны:", message_result.text)

# Значения для блока Two Input Fields
first_value = 123
second_value = 101
sum_result = first_value + second_value

# Находим первое поле и вводим значение
input_first_value = wait.until(EC.element_to_be_clickable((By.ID, "sum1")))
input_first_value.send_keys(first_value)

# Находим второе поле и вводим значение
input_second_value = wait.until(EC.element_to_be_clickable((By.ID, "sum2")))
input_second_value.send_keys(second_value)

# Нажимаем кнопку Get Sum
click_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='gettotal']/button")))
click_button.click()

# Получаем результат сложения
result = wait.until(EC.visibility_of_element_located((By.ID, "addmessage")))

# Сравниваем ожидаемую сумму с результатом на странице
value_result = result.text

assert value_result == str(sum_result), f"Ожидалось {sum_result}, получено {value_result}"

print("Значения равны:", value_result)

time.sleep(3)