from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Chrome
def test_calc(driver):
    wait = WebDriverWait(driver, 50)
    driver.maximize_window()

    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # В поле ввода по локатору #delay введите значение 45.
    field_input = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "#delay")
    ))
    field_input.clear()
    field_input.send_keys("45")

    # Нажмите на кнопки: 7, +, 8, =
    buttons = {
        "//span[text()='7']": "7",
        "//span[text()='+']": "+",
        "//span[text()='8']": "8",
        "//span[text()='=']": "="
    }

    for name, value in buttons.items():
        element = wait.until(EC.presence_of_element_located(
            (By.XPATH, name)
        ))
        element.click()

    wait.until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
    )

    # Проверьте(assert), что в окне отобразится результат 15 через 45 секунд.
    result = driver.find_element(By.CLASS_NAME, "screen")
    assert result.text == "15"

    driver.quit()
