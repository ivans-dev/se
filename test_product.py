import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import re

@pytest.fixture
def driver(request):
    wd = webdriver.Firefox(executable_path=r"C:\tools\geckodriver.exe.exe")
    request.addfinalizer(wd.quit)
    wd.get("http://localhost/")
    WebDriverWait(wd, 20).until(
        lambda x: wd.find_element_by_css_selector("#copyright"))
    return wd


def test_title(driver,):
    name_main_page = driver.find_element_by_css_selector("#box-campaigns div.name").get_attribute("innerText")
    driver.find_element_by_css_selector("#box-campaigns a.link").click()
    name_product_page = driver.find_element_by_css_selector("h1").get_attribute("innerText")
    # Сравнение название товара
    assert name_main_page == name_product_page

def test_price(driver):
    price_main_page = driver.find_element_by_css_selector("#box-campaigns s.regular-price").get_attribute("innerText")
    share_price_main_page = driver.find_element_by_css_selector("#box-campaigns strong.campaign-price").get_attribute("innerText")

    driver.find_element_by_css_selector("#box-campaigns a.link[href]").click()
    share_price_product_page = driver.find_element_by_css_selector("strong.campaign-price").get_attribute("innerText")
    price_product_page = price = driver.find_element_by_css_selector("s.regular-price").get_attribute("innerText")

    # Проверка совпадение цен
    assert (price_main_page == price_product_page) and (share_price_main_page == share_price_product_page)

def test_main_color_price(driver):

    price_color = driver.find_element_by_css_selector("#box-campaigns s.regular-price").value_of_css_property("text-decoration-color")

    price_line = driver.find_element_by_css_selector("#box-campaigns s.regular-price").value_of_css_property("text-decoration-line")
    colors = re.findall(r'\d+', price_color)
    # Проверяем что цвет серый и зачеркнутый (line-through)
    assert (colors == sorted(colors)) and (price_line == "line-through")

def test_product_color_price(driver):
    driver.find_element_by_css_selector("#box-campaigns a.link[href]").click()
    price_color =  driver.find_element_by_css_selector("s.regular-price").value_of_css_property("text-decoration-color")
    price_line = driver.find_element_by_css_selector("s.regular-price").value_of_css_property("text-decoration-line")

    colors = re.findall(r'\d+', price_color)
    # Проверяем что цвет серый и зачеркнутый (line-through)
    assert (colors == sorted(colors)) and (price_line == "line-through")

def test_main_share_price(driver):
    share_price_color = driver.find_element_by_css_selector("#box-campaigns strong.campaign-price").value_of_css_property("text-decoration-color")
    share_price_strong = driver.find_element_by_css_selector("#box-campaigns strong.campaign-price").get_attribute("tagName")
    colors = re.findall(r'\d+', share_price_color)
    R = int(colors[0])
    G = int(colors[1])
    B = int(colors[2])
    # Проверка что красный и жирный
    assert (R > 0 and G == 0 and B == 0) and(share_price_strong == "STRONG")


def test_product_share_price(driver):
    driver.find_element_by_css_selector("#box-campaigns a.link[href]").click()
    share_price_color = driver.find_element_by_css_selector("strong.campaign-price").value_of_css_property("text-decoration-color")
    share_price_strong = driver.find_element_by_css_selector("strong.campaign-price").get_attribute("tagName")
    colors = re.findall(r'\d+', share_price_color)
    R = int(colors[0])
    G = int(colors[1])
    B = int(colors[2])
    # Проверка что красный и жирный
    assert (R > 0 and G == 0 and B == 0) and(share_price_strong == "STRONG")

def test_main_price_size(driver):

    price = re.findall(r'\d*\.\d+|\d+', driver.find_element_by_css_selector("#box-campaigns s.regular-price").value_of_css_property("font-size"))
    share_price =re.findall(r'\d*\.\d+|\d+', driver.find_element_by_css_selector("#box-campaigns strong.campaign-price").value_of_css_property("font-size"))
    # Првоерка размера надписи цен
    assert (float(price[0]) < float(share_price[0]))

def test_product_price_size(driver):
    driver.find_element_by_css_selector("#box-campaigns a.link[href]").click()
    price = re.findall(r'\d*\.\d+|\d+', driver.find_element_by_css_selector("s.regular-price").value_of_css_property("font-size"))
    share_price =re.findall(r'\d*\.\d+|\d+', driver.find_element_by_css_selector("strong.campaign-price").value_of_css_property("font-size"))
    # Првоерка размера надписи цен
    assert (float(price[0]) < float(share_price[0]))