import os
import glob
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Путь к папке, куда будет скачан файл
path_download = "D:\\selen_proj\\files_dow"

# Настройка Chrome
options = webdriver.ChromeOptions()
prefs = {"download.default_directory": path_download}
options.add_experimental_option("prefs", prefs)
options.add_experimental_option("detach", True)

# Запуск браузера
driver = webdriver.Chrome(
    options=options,
    service=ChromeService(ChromeDriverManager().install())
)

# Переход на страницу
base_url = "https://www.lambdatest.com/selenium-playground/download-file-demo"
driver.get(base_url)
driver.set_window_size(1920, 1080)

# Находим кнопку Download File
click_button = driver.find_element(
    By.XPATH,
    "//a[contains(text(), 'Download File')]"
)

# Нажимаем кнопку
click_button.click()

# Ждём загрузку файла
time.sleep(3)

# Название скачанного файла
file_name = "LambdaTest.pdf"

# Формируем полный путь к файлу
file_path = os.path.join(path_download, file_name)

# Сообщение о начале проверки
print("Начинаем проверку скачанного файла")

# Проверяем, что файл существует
assert os.access(file_path, os.F_OK) is True

print("Файл скачался")

# Получаем список файлов в папке загрузки
files = glob.glob(os.path.join(path_download, "*.*"))

# Проверяем размер файла
for file in files:
    file_size = os.path.getsize(file)

    if file_size > 0:
        print("Файл не пуст")
    else:
        print("Файл пуст")

driver.quit()
