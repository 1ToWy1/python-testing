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

# переход на страницу с окнами и вкладками
base_url = 'https://demoqa.com/browser-windows'
driver.get(base_url)

# сохраняем идентификатор исходной вкладки
original_tab = driver.current_window_handle

# сохраняем заголовок исходной вкладки
original_title = driver.title

# --- работа с новой вкладкой ---

# поиск и нажатие кнопки открытия новой вкладки
new_tab_button = wait.until(
    EC.element_to_be_clickable((By.ID, "tabButton"))
)
new_tab_button.click()

# пауза для появления новой вкладки
time.sleep(2)

# переключение на новую вкладку
driver.switch_to.window(driver.window_handles[1])

print('Текущая вкладка:', driver.title)

# переключение обратно на исходную вкладку
driver.switch_to.window(original_tab)

print('Вернулись на вкладку:', driver.title)

# проверка, что мы действительно вернулись на исходную вкладку
assert driver.current_window_handle == original_tab, "Не вернулись на исходную вкладку"

# проверка заголовка исходной вкладки
assert driver.title == original_title, "Заголовок исходной вкладки не совпадает"

print('Вернулись на исходную вкладку успешно')


# --- работа с новым окном ---

# поиск и нажатие кнопки открытия нового окна
new_window_button = wait.until(
    EC.element_to_be_clickable((By.ID, "windowButton"))
)
new_window_button.click()

# пауза для появления нового окна
time.sleep(2)

# переключение на новое окно
driver.switch_to.window(driver.window_handles[2])

print('Текущее окно:', driver.title)

# переключение обратно на исходную вкладку
driver.switch_to.window(original_tab)

print('Вернулись в окно:', driver.title)

# проверка, что мы вернулись на исходную вкладку
assert driver.current_window_handle == original_tab, "Не вернулись на исходную вкладку"

# проверка заголовка исходной вкладки
assert driver.title == original_title, "Заголовок исходной вкладки не совпадает"

print('Вернулись в исходное окно успешно')

# пауза, чтобы визуально увидеть результат
time.sleep(3)

driver.quit()
driver.quit()
