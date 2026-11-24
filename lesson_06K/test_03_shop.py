from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Firefox
def test_shop(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.saucedemo.com/")

    # Авторизуйтесь как пользователь standard_user.
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Добавьте в корзину товары:
    # Sauce Labs Backpack.
    # Sauce Labs Bolt T - Shirt.
    # Sauce Labs Onesie.
    goods = [
        "add-to-cart-sauce-labs-backpack",
        "add-to-cart-sauce-labs-bolt-t-shirt",
        "add-to-cart-sauce-labs-onesie"
    ]

    for good in goods:
        wait.until(EC.element_to_be_clickable((By.ID, good))).click()

    # Перейдите в корзину.
    cart = wait.until(
        EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
    cart.click()

    # Нажмите Checkout.
    checkout_button = wait.until(
        EC.element_to_be_clickable((By.ID, "checkout")))
    checkout_button.click()

    # Заполните форму своими данными:
    # имя,
    # фамилия,
    # почтовый индекс.
    date = {
        "first-name": "Марина",
        "last-name": "Соколова",
        "postal-code": "420065"
    }

    for name, value in date.items():
        field = wait.until(EC.presence_of_element_located((By.ID, name)))
        field.clear()
        field.send_keys(value)

    # Нажмите кнопку Continue.
    continue_button = wait.until(
        EC.element_to_be_clickable((By.ID, "continue")))
    continue_button.click()

    # Прочитайте со страницы итоговую стоимость(Total).
    total = wait.until(EC.visibility_of_element_located(
        (By.CLASS_NAME, "summary_total_label")
    ))

    total_text = total.text

    # Закройте браузер.
    driver.quit()

    # Проверьте, что итоговая сумма равна $58.29.
    assert total_text == "Total: $58.29"
