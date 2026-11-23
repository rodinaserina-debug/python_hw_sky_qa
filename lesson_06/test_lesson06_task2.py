# Тест 2. Работа с cookie
#
# Предварительные шаги:
# Создано два аккаунта на https://gitflic.ru/:
#   пользователь 1: login - yi5gnr@uqu.me  (test9);      password - 67890Qwerty
#   пользователь 2: login - in6vq@airsworld.net (airsworld); password - 12345Qwerty
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 20)
    # Откройте страницу https://gitflic.ru/.
    driver.get("https://gitflic.ru/")

    # Установите cookie пользователя 1 (test9)
    driver.add_cookie({
            "name": "SESSION",
            "value": "YzE1NWFmNGEtZTY2OS00YjI4LWI4ZTQtODdiZTM3ZTc4ZjY0",
            "domain": "gitflic.ru",
    })

    driver.add_cookie({
            "name": "cookiesAccepted",
            "value": "true",
            "domain": "gitflic.ru"
    })

    # Обновите страницу.
    driver.refresh()

    # Перейдите на страницу пользователя 1.
    driver.get("https://gitflic.ru/user/test9")
    wait.until(EC.url_contains("/test9"))

    # Сохраните текущий URL.
    url_user_one = driver.current_url

    # Разлогиньтесь (очистите куки).
    driver.delete_all_cookies()
    driver.refresh()

    driver.get("https://gitflic.ru/")

    # Установите cookie пользователя 2 (airsworld)
    driver.add_cookie({
            "name": "SESSION",
            "value": "YTNlM2I5MGEtMGZlYy00MzQ3LTgyYzctMmM5OTMxZmQzODk4",
            "domain": "gitflic.ru",
    })

    driver.add_cookie({
            "name": "cookiesAccepted",
            "value": "true",
            "domain": "gitflic.ru"
    })

    # Обновите страницу.
    driver.refresh()

    # Перейдите на страницу пользователя 2.
    driver.get("https://gitflic.ru/user/airsworld")
    wait.until(EC.url_contains("/airsworld"))

    # Сохраните текущий URL.
    login_user_two = driver.current_url

    # Проверьте, что URL для пользователя 1 и пользователя 2 различаются.
    assert url_user_one != login_user_two

    driver.quit()
