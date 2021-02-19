import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome(r'c:\tools\chromedriver.exe')
    request.addfinalizer(wd.quit)
    return wd

def test_yandex(driver):
    driver.get("https://yandex.ru/")
    driver.find_element_by_name("text").send_keys("Hello World")
    driver.find_element_by_xpath("//button[@type='submit']").click()
    WebDriverWait(driver, 10).until(
        lambda x: driver.execute_script('return document.readyState') == 'complete')