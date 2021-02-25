import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time

@pytest.fixture
def driver(request):
    wd = webdriver.Firefox(executable_path=r"C:\tools\geckodriver.exe")
    request.addfinalizer(wd.quit)
    wd.get("http://localhost/admin/login.php")
    wd.find_element_by_name("username").send_keys("admin")
    wd.find_element_by_name("password").send_keys("admin")
    wd.find_element_by_name("login").click()
    return wd

def links(driver):
    return  list((element.get_attribute('href') for element in driver.find_elements_by_css_selector("li#app- >a")))
def sub_links(driver):
    return list((element.get_attribute('href') for element in driver.find_elements_by_css_selector("li[id^=doc-] >a")))

def test_menu(driver):
    elements = links(driver)
    for url in elements:
        driver.find_element_by_xpath('//a[@href="'+url+'"]').click()
        sub_elements = sub_links(driver)
        if  len(sub_elements)==0:
            WebDriverWait(driver, 10).until(
            lambda x: driver.find_element_by_css_selector("#content > h1"))
            assert driver.find_element_by_css_selector("#content > h1")
            continue
        for sub_url in sub_elements:
            driver.find_element_by_xpath('//a[@href="'+sub_url+'"]').click()
            WebDriverWait(driver, 10).until(
            lambda x: driver.find_element_by_css_selector("#content > h1"))
            assert driver.find_element_by_css_selector("#content > h1")