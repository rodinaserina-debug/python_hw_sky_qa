from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Edge
def test_form(driver):
    wait = WebDriverWait(driver, 10)
    driver.maximize_window()

    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Заполните форму значениями:
    form_data = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "zip-code": "",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro",
    }

    for name, value in form_data.items():
        field = wait.until(
            EC.presence_of_element_located((By.NAME, name)))
        field.clear()
        field.send_keys(value)

    # Нажмите кнопку Submit.
    submit_button = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "btn-outline-primary")))
    submit_button.click()

    # Проверьте(assert), что поле Zip code подсвечено красным.
    zip_code_field = wait.until(
        EC.presence_of_element_located((By.ID, "zip-code")))
    assert "alert-danger" in zip_code_field.get_attribute("class")
    print(f"Поле Zip code подсвечено красным, класс: {
        zip_code_field.get_attribute('class')}")

    # Проверьте(assert), что остальные поля подсвечены зеленым.
    for name in ["first-name", "last-name", "address", "e-mail", "phone",
                 "city", "country", "job-position", "company"]:
        field = wait.until(
            EC.presence_of_element_located((By.ID, name)))
        assert "alert-success" in field.get_attribute("class")
        print(f"Это поле подсвечено зеленым, класс: {
                field.get_attribute('class')}")

    driver.quit()
