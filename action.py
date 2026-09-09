import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
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
options.add_experimental_option("detach", True)  # чтобы браузер не закрывался автоматически

# инициализация веб-драйвера
driver = webdriver.Chrome(
    options=options,
    service=ChromeService(ChromeDriverManager().install())
)

# разворачивание окна браузера на весь экран
driver.maximize_window()

# переход на страницу с кнопками
base_url = 'https://demoqa.com/buttons'
driver.get(base_url)

# создание экземпляра класса ActionChains для выполнения действий мыши
action = ActionChains(driver)

# Тест иногда падает, на перед проверяю несколько раз
for i in range(5):
    try:
        # поиск кнопки для двойного клика
        double_click_button = driver.find_element(By.ID, "doubleClickBtn")
        time.sleep(2)
        # выполнение двойного клика по кнопке
        action.double_click(double_click_button).perform()

        # поиск сообщения после двойного клика
        double_click_message = driver.find_element(By.ID, "doubleClickMessage")

        # проверка текста сообщения после двойного клика
        assert double_click_message.text == "You have done a double click"

        print('Произведен двойной клик')

        # поиск кнопки для правого клика
        right_click_button = driver.find_element(By.ID, "rightClickBtn")

        # выполнение правого клика по кнопке
        action.context_click(right_click_button).perform()

        # поиск сообщения после правого клика
        right_click_message = driver.find_element(By.ID, "rightClickMessage")

        # проверка текста сообщения после правого клика
        assert right_click_message.text == "You have done a right click"

        print('Произведен правый клик')
        print('Количество пройденных тестов:', i + 1,)
    except AssertionError:
        print('Тест провален', i + 1)

# небольшая задержка для отображения результата
time.sleep(2)
driver.quit()
