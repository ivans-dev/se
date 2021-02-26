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
    styles = ('box-most-popular', 'box-campaigns', 'box-latest-products')
    for style in styles:
        base_elem = driver.find_element_by_css_selector('#' + style + '> div > ul')
        all_duck = base_elem.find_elements_by_css_selector('li')
        i = 1
        while i <= len(all_duck):
            all_sticker = base_elem.find_elements_by_css_selector('li:nth-child(' + str(
                i) + ')> a.link > div.image-wrapper > '                                                                          'div')
            i += 1

            #print(style + "  " + str(len(all_sticker))) для проверки
            assert len(all_sticker) == 1
