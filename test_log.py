import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time


@pytest.fixture(autouse=True)
def driver(request):
    driver = webdriver.Chrome(executable_path=r"C:\tools\chromedriver.exe")
    request.addfinalizer(driver.quit)
    driver.get("http://localhost/admin/?app=catalog&doc=catalog")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    WebDriverWait(driver, 10).until(
        lambda x: driver.find_element_by_css_selector("#copyright"))
    return driver


def links(driver):
    elements = driver.find_elements_by_css_selector("#content > form > table > tbody > tr > td:nth-child(3) > a")
    links = []
    for element in elements:
        links.append(element.get_attribute("href"))
    del links[0]
    return links


def test_log(driver):
    for link in links(driver):
        driver.get(link)
        time.sleep(1)
        log = driver.get_log("browser")
        assert len(log) == 0, print("Лог: " + str(log)) # Проверяем и в случае падения выводим лог
