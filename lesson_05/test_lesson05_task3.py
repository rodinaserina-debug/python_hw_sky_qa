from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/links/10")

    links = driver.find_elements(By.TAG_NAME, "a")
    assert len(links) == 9
    print(f"Получилось ссылок: {len(links)}")

    for link in links:
        assert link.is_displayed()
        print(f"Ссылка {link.text} отображается")

    assert links[0].text == "1"
    print(f"Текст первой ссылки: {links[0].text}")

    driver.quit()
