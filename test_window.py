import pytest
from selenium import webdriver
from selenium.webdriver.support import wait
from selenium.webdriver.support.wait import WebDriverWait
import time


@pytest.fixture
def driver(request):
    driver = webdriver.Chrome(executable_path=r"C:\tools\chromedriver.exe")
    request.addfinalizer(driver.quit)
    driver.get("http://localhost/admin/login.php")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    WebDriverWait(driver, 10).until(
        lambda x: driver.find_element_by_css_selector("#copyright"))
    return driver


def test_windows(driver):
    main_window = driver.current_window_handle
    old_windows = driver.window_handles
    driver.get("http://localhost/admin/?app=countries&amp;doc=countries")
    driver.find_element_by_css_selector(
        "#content > form > table > tbody > tr:nth-child(177) > td:nth-child(5) > a").click()
    links = driver.find_elements_by_css_selector("tbody a[target='_blank']")
    for link in links:
        link.click()
        WebDriverWait(driver, 10).until(lambda driver:len(old_windows) != len(driver.window_handles))
        new_window = windows_name(main=main_window, now=driver.window_handles)
        print(new_window)
        driver.switch_to_window(new_window)
        time.sleep(2)
        driver.close()
        driver.switch_to_window(main_window)
    time.sleep(5)


def windows_name(main, now):
    handle = ""
    for win in now:
        if win == main:
            continue
        handle =  win
    return  handle
