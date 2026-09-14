from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Настройка Chrome
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

# Запуск браузера
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

# Явное ожидание
wait = WebDriverWait(driver, 10)

# Переход на страницу
driver.get("https://www.lambdatest.com/selenium-playground/jquery-dropdown-search-demo")

# Кликаем по Dropdown "Select Country"
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#country + span"))).click()

# Выбираем страну India
wait.until(EC.element_to_be_clickable((By.XPATH, "//ul[@id='select2-country-results']//li[text()='India']"))).click()

# Проверяем выбранное значение
selected_country = wait.until(EC.visibility_of_element_located((By.ID, "select2-country-container")))

assert selected_country.text == "India", "Страна India не выбрана"

print("Выбрана страна:", selected_country.text)

# Закрытие браузера
driver.quit()
