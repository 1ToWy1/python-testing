import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# настройка параметров браузера chrome
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

# инициализация веб-драйвера
driver = webdriver.Chrome(
    options=options,
    service=ChromeService(ChromeDriverManager().install())
)

# установка размера окна браузера
driver.set_window_size(width=1920, height=1080)

# явное ожидание
wait = WebDriverWait(driver, 10)

# переход на страницу с алертами
base_url = 'https://the-internet.herokuapp.com/javascript_alerts'
driver.get(base_url)

# ---простой JS Alert---

# поиск и нажатие кнопки вызова простого алерта
alert_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Click for JS Alert']")))
alert_btn.click()

# переключение на алерт и подтверждение
alert = driver.switch_to.alert
print('Текст алерта:', alert.text)
alert.accept()

# проверка результата после закрытия алерта
result = wait.until(EC.visibility_of_element_located((By.ID, "result")))
assert result.text == "You successfully clicked an alert", "Ошибка: неверный результат после JS Alert"
print('Результат:', result.text)

time.sleep(1)

# ---2. JS Confirm---

# поиск и нажатие кнопки вызова confirm-алерта
confirm_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Click for JS Confirm']")))
confirm_btn.click()

# переключение на алерт и отмена (нажатие Cancel)
confirm_alert = driver.switch_to.alert
print('Текст конфирма:', confirm_alert.text)
confirm_alert.dismiss()

# проверка результата после отмены
result = wait.until(EC.visibility_of_element_located((By.ID, "result")))
assert result.text == "You clicked: Cancel", "Ошибка: неверный результат после Cancel"
print('Результат:', result.text)

time.sleep(1)

# ---3. JS Prompt---

# поиск и нажатие кнопки вызова prompt-алерта
prompt_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Click for JS Prompt']")))
prompt_btn.click()

# переключение на алерт, ввод текста и подтверждение
prompt_alert = driver.switch_to.alert
prompt_alert.send_keys("Привет, Selenium!")
prompt_alert.accept()

# проверка результата после ввода текста
result = wait.until(EC.visibility_of_element_located((By.ID, "result")))
assert result.text == "You entered: Привет, Selenium!", "Ошибка: неверный результат после Prompt"
print('Результат:', result.text)

driver.quit()