import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def driver(request):
    wd = webdriver.Firefox(executable_path=r"C:\tools\geckodriver.exe")
    request.addfinalizer(wd.quit)
    wd.get("http://localhost/")
    WebDriverWait(wd, 10).until(
        lambda x: wd.find_element_by_css_selector("#copyright"))
    return wd


def test_sticker(driver):
    all_products = driver.find_elements_by_css_selector("li.product")
    all_stickers = driver.find_elements_by_css_selector("li.product div.sticker")
    assert len(all_products) == len(all_stickers)