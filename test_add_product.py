import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from faker import Faker
import os
import time

@pytest.fixture
def driver(request):
    driver = webdriver.Firefox(executable_path=r"C:\tools\geckodriver.exe")
    request.addfinalizer(driver.quit)
    driver.get("http://localhost/admin/login.php")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    WebDriverWait(driver, 10).until(
        lambda x: driver.find_element_by_css_selector("#copyright"))
    return driver


def test_add_product(driver):
    fake = Faker()
    name  = fake.unique.name()
    time.sleep(2)
    driver.find_element_by_css_selector("ul#box-apps-menu li:nth-child(2)").click()
    driver.find_element_by_css_selector("#content a.button:nth-child(2)").click()
    driver.find_element_by_xpath('//*[@id="tab-general"]/table/tbody/tr[1]/td/label[1]/input').click()
    driver.find_element_by_css_selector("#tab-general span.input-wrapper input[name ^='name'").click()
    driver.find_element_by_css_selector("#tab-general span.input-wrapper input[name ^='name'").clear()
    driver.find_element_by_css_selector("#tab-general span.input-wrapper input[name ^='name'").send_keys(name)
    driver.find_element_by_css_selector("#tab-general tr:nth-child(3) input[name='code']").click()
    driver.find_element_by_css_selector("#tab-general tr:nth-child(3) input[name='code']").clear()
    driver.find_element_by_css_selector("#tab-general tr:nth-child(3) input[name='code']").send_keys("666")
    driver.find_element_by_css_selector("#tab-general tr:nth-child(4) input[data-name='Rubber Ducks']").click()
    driver.find_element_by_css_selector("#tab-general div.input-wrapper input[value='1-3']").click()
    driver.find_element_by_css_selector("#tab-general input[name='quantity']").click()
    driver.find_element_by_css_selector("#tab-general input[name='quantity']").clear()
    driver.find_element_by_css_selector("#tab-general input[name='quantity']").send_keys("999")
    driver.find_element_by_css_selector("#tab-general input[type='file']").send_keys(file())
    element = driver.find_element_by_css_selector("#tab-general input[name='date_valid_from']")
    date="01/01/2021"
    driver.execute_script('arguments[0].setAttribute("value", "%s")' % date, element)
    element = driver.find_element_by_css_selector("#tab-general input[name='date_valid_to']")
    date="01/01/2022"
    driver.execute_script('arguments[0].setAttribute("value", "%s")' % date, element)
    driver.find_element_by_css_selector("ul.index a[href='#tab-information").click()
    time.sleep(1)
    select = driver.find_element_by_css_selector("#tab-information select[name='manufacturer_id']")
    driver.execute_script("arguments[0].setAttribute('class','')", select)
    Select(select).select_by_visible_text('ACME Corp.')
    driver.find_element_by_css_selector("#tab-information > table > tbody > tr:nth-child(3) > td > input[type=text]").click()
    driver.find_element_by_css_selector("#tab-information > table > tbody > tr:nth-child(3) > td > input[type=text]").clear()
    driver.find_element_by_css_selector("#tab-information > table > tbody > tr:nth-child(3) > td > input[type=text]").send_keys("Testing duck")
    driver.find_element_by_css_selector("#tab-information > table > tbody > tr:nth-child(4) > td > span > input[type=text]").click()
    driver.find_element_by_css_selector("#tab-information > table > tbody > tr:nth-child(4) > td > span > input[type=text]").clear()
    driver.find_element_by_css_selector("#tab-information > table > tbody > tr:nth-child(4) > td > span > input[type=text]").send_keys("Testing duck best dcuk")
    driver.find_element_by_css_selector("#tab-information > table > tbody > tr:nth-child(5) > td > span > div > div.trumbowyg-editor").click()
    driver.find_element_by_css_selector("#tab-information > table > tbody > tr:nth-child(5) > td > span > div > div.trumbowyg-editor").clear()
    driver.find_element_by_css_selector("#tab-information > table > tbody > tr:nth-child(5) > td > span > div > div.trumbowyg-editor").send_keys("Bla bla bla duck")
    driver.find_element_by_css_selector("#tab-information > table > tbody > tr:nth-child(6) > td > span > input[type=text]").click()
    driver.find_element_by_css_selector("#tab-information > table > tbody > tr:nth-child(6) > td > span > input[type=text]").clear()
    driver.find_element_by_css_selector("#tab-information > table > tbody > tr:nth-child(6) > td > span > input[type=text]").send_keys("Testing duck duck")
    driver.find_element_by_css_selector("#tab-information > table > tbody > tr:nth-child(7) > td > span > input[type=text]").click()
    driver.find_element_by_css_selector("#tab-information > table > tbody > tr:nth-child(7) > td > span > input[type=text]").clear()
    driver.find_element_by_css_selector("#tab-information > table > tbody > tr:nth-child(7) > td > span > input[type=text]").send_keys("Testing duck duck")
    driver.find_element_by_css_selector("ul.index a[href='#tab-prices").click()
    time.sleep(1)
    driver.find_element_by_css_selector("#tab-prices > table:nth-child(2) > tbody > tr > td > input[type=number]").click()
    driver.find_element_by_css_selector("#tab-prices > table:nth-child(2) > tbody > tr > td > input[type=number]").clear()
    driver.find_element_by_css_selector("#tab-prices > table:nth-child(2) > tbody > tr > td > input[type=number]").send_keys("100")
    driver.find_element_by_css_selector("#tab-prices > table:nth-child(4) > tbody > tr:nth-child(2) > td:nth-child(1) > span > input[type=text]").click()
    driver.find_element_by_css_selector("#tab-prices > table:nth-child(4) > tbody > tr:nth-child(2) > td:nth-child(1) > span > input[type=text]").clear()
    driver.find_element_by_css_selector("#tab-prices > table:nth-child(4) > tbody > tr:nth-child(2) > td:nth-child(1) > span > input[type=text]").send_keys("20")
    driver.find_element_by_css_selector("#tab-prices > table:nth-child(4) > tbody > tr:nth-child(2) > td:nth-child(2) > input[type=number]").click()
    driver.find_element_by_css_selector("#tab-prices > table:nth-child(4) > tbody > tr:nth-child(2) > td:nth-child(2) > input[type=number]").clear()
    driver.find_element_by_css_selector("#tab-prices > table:nth-child(4) > tbody > tr:nth-child(2) > td:nth-child(2) > input[type=number]").send_keys("3")
    driver.find_element_by_css_selector("#content > form > p > span > button:nth-child(1)").click()
    time.sleep(2)
    elements = driver.find_elements_by_css_selector("table.dataTable tbody tr td:nth-child(3) a")
    names = [elem.get_attribute('innerText') for elem in elements]
    assert name in names
    time.sleep(3)



def file():
    dir = os.path.dirname(__file__)
    return os.path.join(dir,"img\duck.png")









































































































































































































    time.sleep(10)
