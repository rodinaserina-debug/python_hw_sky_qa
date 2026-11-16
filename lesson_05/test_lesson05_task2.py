from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/forms/post")

    input_name = driver.find_element(By.NAME, "custname")
    input_name.send_keys("Родина Ирина")

    button = driver.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

    assert driver.current_url == (
            "https://httpbin.qa-territory.online/forms/post")

    driver.quit()
