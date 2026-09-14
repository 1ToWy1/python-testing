from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(
    options=options,
    service=ChromeService(ChromeDriverManager().install())
)

wait = WebDriverWait(driver, 10)

driver.get("https://the-internet.herokuapp.com/horizontal_slider")

# Находим ползунок
slider = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='range']")))

ActionChains(driver).move_to_element(slider).click_and_hold().move_by_offset(50, 0).release().perform()

slider_value = wait.until(EC.presence_of_element_located((By.ID, "range")))

print(f"Значение после перемещения мышью: {slider_value.text}")

assert slider_value.text == "4.5", f"Ожидалось 4.5, получено {slider_value.text}"


# Второй сценарий — начинаем заново
driver.refresh()

slider = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='range']")))

slider.click()
slider.send_keys(Keys.HOME)

# 5 шагов вправо
for _ in range(5):
    slider.send_keys(Keys.ARROW_RIGHT)

slider_value = wait.until(EC.presence_of_element_located((By.ID, "range")))

print(f"Значение после 5 нажатий: {slider_value.text}")

assert slider_value.text == "2.5", f"Ожидалось 2.5, получено {slider_value.text}"