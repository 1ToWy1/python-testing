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

# путь к твоему файлу
path_upload = "D:\\selen_proj\\moyfail.png"
expected_name = os.path.basename(path_upload)  # получаем "moyfail.png"

# находим поле загрузки
upload_field = wait.until(
    EC.presence_of_element_located((By.XPATH, "//input[@id='file']"))
)

# загружаем файл
upload_field.send_keys(path_upload)
print("Файл отправлен на загрузку")

# ждем появления сообщения об успехе (это единственный видимый текст на странице)
wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//*[contains(text(), 'File Successfully Uploaded')]")
    )
)

# ПОЛУЧАЕМ ИМЯ ФАЙЛА ИЗ АТРИБУТА VALUE
actual_name = upload_field.get_attribute("value")

# Извлекаем только имя файла из полного пути (если там оказался путь C:\fakepath\...)
if "\\" in actual_name or "/" in actual_name:
    actual_name = os.path.basename(actual_name)

# проверяем совпадение
assert actual_name == expected_name, (
    f"Ошибка: имя не совпадает. Ожидалось '{expected_name}', в поле загрузки '{actual_name}'"
)

print(f"Имя файла совпадает: {actual_name}")

driver.quit()
