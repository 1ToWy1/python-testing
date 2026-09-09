import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# настройка параметров браузера chrome
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

# отключение политики проверки утечки паролей и сохраненных паролей chrome
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

# переход на страницу с радиокнопками
base_url = 'https://demoqa.com/radio-button'
driver.get(base_url)

time.sleep(2)

# 1. выбор радиокнопки
yes_label = driver.find_element(By.XPATH, "//label[@for='yesRadio']")
yes_label.click()
print("Нажато на радиокнопку Yes")

time.sleep(1)

# проверка состояния радиокнопки через элемент input
yes_radio_input = driver.find_element(By.ID, "yesRadio")
assert yes_radio_input.is_selected(), "Ошибка: радиокнопка Yes не выбрана"
print("Проверка успешна: радиокнопка Yes выбрана (is_selected() == True)")

# проверка текста в блоке результатов под радиокнопками
result_text = driver.find_element(By.CLASS_NAME, "text-success").text
assert result_text == "Yes", f"Ошибка: ожидался текст 'Yes', но получен '{result_text}'"
print(f"Текст результата подтверждает выбор: {result_text}")

time.sleep(1)

# закрытие браузера и завершение сессии
driver.quit()
