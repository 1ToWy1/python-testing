import time
import os

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

# явное ожидание
wait = WebDriverWait(driver, 10)

# переход на страницу загрузки файлов
base_url = 'https://www.lambdatest.com/selenium-playground/upload-file-demo'
driver.get(base_url)

# путь к файлу, который будем загружать
path_upload = "D:\\selen_proj\\img.png"

# сохраняем исходное имя файла для проверки
file_name = os.path.basename(path_upload)

# правильный id поля загрузки - "file-input", а не "file"
upload_field = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//input[@id='file-input']"))
)

# загружаем файл через send_keys
upload_field.send_keys(path_upload)
print("Файл отправлен на загрузку")

# пауза для завершения загрузки и обновления UI
time.sleep(3)

# проверяем, что имя файла отображается на странице после загрузки
uploaded_file = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, f"//*[contains(text(), '{file_name}')]")
    )
)

uploaded_file_name = uploaded_file.text.strip()

# сравниваем имя загруженного файла с исходным
assert uploaded_file_name == file_name, (
    f"Ошибка: имя файла не совпадает. "
    f"Ожидалось '{file_name}', получено '{uploaded_file_name}'"
)

print("Имя файла совпадает:", uploaded_file_name)

driver.quit()
