# Тест 1. Ожидание динамической загрузки данных
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Шаги:
# Откройте страницу https://the-internet.herokuapp.com/dynamic_loading/2.
def test_dynamic_loading():
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

    # Найдите и нажмите на кнопку Start.
    start_btn = driver.find_element(By.CSS_SELECTOR, "#start button")
    start_btn.click()

    # Дождитесь появления текста Hello World!
    hello_text = wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#finish h4")
    ))

    # Сделайте скриншот страницы
    driver.save_screenshot("lesson_06/screenshots/full_screen.png")

    # Проверьте, что появившийся текст равен "Hello World!"
    assert hello_text.text == "Hello World!"

    driver.quit()
