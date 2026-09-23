from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

# настройка параметров браузера chrome
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

# инициализация веб-драйвера
driver = webdriver.Chrome(
    options=options,
    service=ChromeService(ChromeDriverManager().install())
)

# явное ожидание
wait = WebDriverWait(driver, 10)

# переход на страницу с динамическими свойствами
base_url = 'https://demoqa.com/dynamic-properties'
driver.get(base_url)

try:
    # попытка нажать на невидимую кнопку до появления
    hidden_button = driver.find_element(By.ID, "visibleAfter")
    hidden_button.click()

except NoSuchElementException:
    print("Кнопка невидима, ожидаем")

    # ждем пока кнопка станет кликабельной
    visible_button = wait.until(EC.element_to_be_clickable((By.ID, "visibleAfter")))
    visible_button.click()
    print("Кнопка успешно нажата после ожидания")

driver.quit()
