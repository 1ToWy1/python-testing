from datetime import datetime, timedelta
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


# Настройка параметров Chrome
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

# Отключение политики проверки утечки паролей
prefs = {
    "profile.password_manager_leak_detection": False,
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
}

options.add_experimental_option("prefs", prefs)

# Инициализация WebDriver
driver = webdriver.Chrome(
    options=options,
    service=ChromeService(ChromeDriverManager().install())
)

driver.maximize_window()

# Явное ожидание
wait = WebDriverWait(driver, 10)

# Переход на страницу Date Picker
driver.get("https://demoqa.com/date-picker")


# Создаём дату, которая на 10 дней позже текущей
current_date = datetime.now()
future_date = current_date + timedelta(days=10)

# Преобразуем дату в формат MM/DD/YYYY
date_to_enter = future_date.strftime("%d/%m/%Y")

# Находим поле даты
date_input = wait.until(
    EC.element_to_be_clickable((By.ID, "datePickerMonthYearInput"))
)

# Очищаем поле и вводим рассчитанную дату
date_input.click()
date_input.send_keys(Keys.CONTROL + "a")
date_input.send_keys(date_to_enter)

# Проверяем, что нужная дата введена
assert date_input.get_attribute("value") == date_to_enter, "В поле введена неправильная дата"

print(f"Текущая дата: {current_date.strftime('%d.%m.%Y')}")
print(f"Дата через 10 дней: {date_to_enter}")

# Закрываем браузер
driver.quit()
