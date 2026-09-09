import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# настройка параметров браузера chrome
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

# отключение политики проверки утечки паролей и сохраненных паролей
prefs = {
    "profile.password_manager_leak_detection": False,
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
}
options.add_experimental_option("prefs", prefs)
options.add_experimental_option("detach", True)  # чтобы браузер не закрывался автоматически

# инициализация веб-драйвера
driver = webdriver.Chrome(
    options=options,
    service=ChromeService(ChromeDriverManager().install())
)

# разворачивание окна браузера на весь экран
driver.maximize_window()

# переход на страницу с чекбоксами
base_url = 'https://demoqa.com/checkbox'
driver.get(base_url)

time.sleep(2)

# выбор чекбокса по вашему xpath
desktop_checkbox_label = driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div/div[2]/div[1]/div/div[3]/div/div/div/div/span[3]')
desktop_checkbox_label.click()
print("Нажато на чекбокс Desktop")

time.sleep(1)


aria_checked_value = desktop_checkbox_label.get_attribute("aria-checked")

# проверка, что aria-checked равен "true"
assert aria_checked_value == "true", f"Ошибка: чекбокс не выбран, aria-checked = '{aria_checked_value}'"
print("Проверка успешна: чекбокс выбран (aria-checked == 'true')")

time.sleep(3)

# закрытие браузера и завершение сессии
driver.quit()
