import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def driver(request):
    driver = webdriver.Firefox(executable_path=r"C:\tools\geckodriver.exe")
    request.addfinalizer(driver.quit)
    driver.get("http://localhost/admin/?app=countries&doc=countries")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    WebDriverWait(driver, 10).until(
        lambda x: driver.find_element_by_css_selector("#copyright"))
    return driver

#Проверка расположение стран согласно алфовитному порядку задание 8 ч.1 а
def test_country(driver):
    country = driver.find_elements_by_css_selector("tr.row td:nth-child(5) a[href]")
    list_country = list(element.get_attribute("innerText") for element in country)
    assert sorted(list_country) == list_country

#Проверка расположение зон согласно алфовитному порядку, в странах где есть зоны задание 8 ч.1 б
def test_zone_coutry(driver):
    country = driver.find_elements_by_css_selector("tr.row td:nth-child(5) a[href]")
    zones = driver.find_elements_by_css_selector("tr.row td:nth-child(6)")
    links = []
    i = 0
    for zone in list(element.get_attribute("innerText") for element in zones):
        if zone != "0":
            links.append(country[i].get_attribute("href"))
        i += 1

    for link  in links:
        l_zone = []
        driver.get(link)
        zones = driver.find_elements_by_css_selector("#table-zones tbody td:nth-child(3)")
        for zone in zones:
            if zone.get_attribute("innerText") =="":
                continue
            l_zone.append(zone.get_attribute("innerText"))

        assert sorted(l_zone) == l_zone

#Проверка расположение зон в алфовитном порядке в странах задание 8 ч.2
def test_zone (driver):
    country = driver.find_elements_by_css_selector("tbody > tr > td:nth-child(3) > a")
    links=[]

    for link in country:
        links.append(link.get_attribute("href"))

    for link in links:
        list_zone=[]
        driver.get(link)
        zones = driver.find_elements_by_css_selector("#table-zones tr td:nth-child(3) option[selected='selected']")
        for zone in zones:
            list_zone.append(zone.get_attribute("innerText"))

        assert sorted(list_zone) == list_zone


