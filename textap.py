from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
import time

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

# переход на страницу загрузки файлов
base_url = 'https://www.lambdatest.com/selenium-playground/upload-file-demo'
driver.get(base_url)

path_upload = "D:\\selen_proj\\img.png"
click_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id ='file']")))
click_button.send_keys(path_upload)

success_message = driver.find_element(By.XPATH, "//*[contains(text(), 'File Successfully Uploaded')]")
actual_text = success_message.text.strip()

assert "File Successfully Uploaded" in actual_text, (
    f"Ошибка: сообщение об успехе не найдено. Ожидалось 'File Successfully Uploaded', получено '{actual_text}'")
print("Проверка пройдена: File Successfully Uploaded отображается корректно")

driver.quit()
