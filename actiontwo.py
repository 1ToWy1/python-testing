import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
options.add_experimental_option("detach", True)


# инициализация веб-драйвера
driver = webdriver.Chrome(
    options=options,
    service=ChromeService(ChromeDriverManager().install())
)

# разворачивание окна браузера на весь экран
driver.maximize_window()

# явное ожидание
wait = WebDriverWait(driver, 10)

# переход на страницу с кнопками
base_url = 'https://demoqa.com/buttons'
driver.get(base_url)

# создание экземпляра класса ActionChains
action = ActionChains(driver)


# поиск кнопки для двойного клика
double_click_button = wait.until(
    EC.element_to_be_clickable((By.ID, "doubleClickBtn"))
)

# выполнение двойного клика по кнопке
action.double_click(double_click_button).perform()

# ожидание сообщения после двойного клика
double_click_message = wait.until(
    EC.visibility_of_element_located((By.ID, "doubleClickMessage"))
)

# проверка текста сообщения после двойного клика
assert double_click_message.text == "You have done a double click"

print('Произведен двойной клик')


# поиск кнопки для правого клика
right_click_button = wait.until(
    EC.element_to_be_clickable((By.ID, "rightClickBtn"))
)

# выполнение правого клика по кнопке
action.context_click(right_click_button).perform()

# ожидание сообщения после правого клика
right_click_message = wait.until(
    EC.visibility_of_element_located((By.ID, "rightClickMessage"))
)

# проверка текста сообщения после правого клика
assert right_click_message.text == "You have done a right click"

print('Произведен правый клик')


# небольшая задержка для отображения результата
time.sleep(2)

driver.quit()
