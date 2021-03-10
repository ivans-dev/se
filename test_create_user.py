import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import faker
import time
import random


@pytest.fixture
def driver(request):
    driver = webdriver.Firefox(executable_path=r"C:\tools\geckodriver.exe")
    request.addfinalizer(driver.quit)
    driver.get("http://localhost/en/create_account")
    WebDriverWait(driver, 20).until(
        lambda x: driver.find_element_by_css_selector("#copyright"))
    return driver

password=""
email=""
def test_add_users(driver):
    fake = faker.Faker()
    fake.seed_locale('en_US')
    global email
    global password
    tax_id = fake.unique.ssn()
    company = fake.unique.company()
    first_name = fake.unique.first_name_male()
    last_name = fake.unique.last_name_female()
    address = fake.unique.street_address()
    address2 = fake.unique.street_address()
    postcode = fake.unique.postcode()
    city = fake.unique.city()
    email = fake.unique.ascii_company_email()
    phone = fake.unique.msisdn()
    password = fake.unique.password(length=12)

    driver.find_element_by_name("tax_id").click()
    driver.find_element_by_name("tax_id").clear()
    driver.find_element_by_name("tax_id").send_keys(tax_id)

    driver.find_element_by_name("company").click()
    driver.find_element_by_name("company").clear()
    driver.find_element_by_name("company").send_keys(company)

    driver.find_element_by_name("firstname").click()
    driver.find_element_by_name("firstname").clear()
    driver.find_element_by_name("firstname").send_keys(first_name)

    driver.find_element_by_name("lastname").click()
    driver.find_element_by_name("lastname").clear()
    driver.find_element_by_name("lastname").send_keys(last_name)

    driver.find_element_by_name("address1").click()
    driver.find_element_by_name("address1").clear()
    driver.find_element_by_name("address1").send_keys(address)

    driver.find_element_by_name("address2").click()
    driver.find_element_by_name("address2").clear()
    driver.find_element_by_name("address2").send_keys(address2)

    driver.find_element_by_name("postcode").click()
    driver.find_element_by_name("postcode").clear()
    driver.find_element_by_name("postcode").send_keys(postcode)

    driver.find_element_by_name("city").click()
    driver.find_element_by_name("city").clear()
    driver.find_element_by_name("city").send_keys(city)



    select= driver.find_element_by_class_name("select2-hidden-accessible")
    driver.execute_script("arguments[0].setAttribute('class','')", select)
    Select(select).select_by_visible_text('United States')

    time.sleep(2)
    select = driver.find_element_by_css_selector("select[name='zone_code']")
    Select(select).select_by_value("AK")

    driver.find_element_by_name("email").click()
    driver.find_element_by_name("email").clear()
    driver.find_element_by_name("email").send_keys(email)

    driver.find_element_by_name("email").click()
    driver.find_element_by_name("email").clear()
    driver.find_element_by_name("email").send_keys(email)

    driver.find_element_by_name("phone").click()
    driver.find_element_by_name("phone").clear()
    driver.find_element_by_name("phone").send_keys(phone)

    driver.find_element_by_name("password").click()
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys(password)

    driver.find_element_by_name("confirmed_password").click()
    driver.find_element_by_name("confirmed_password").clear()
    driver.find_element_by_name("confirmed_password").send_keys(password)
    driver.find_element_by_name("create_account").click()
    time.sleep(2)
    driver.find_element_by_link_text("Logout").click()


    driver.find_element_by_name("email").click()
    driver.find_element_by_name("email").clear()
    driver.find_element_by_name("email").send_keys(email)
    driver.find_element_by_name("password").click()
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_name("login").click()
    time.sleep(2)
    driver.find_element_by_link_text("Logout").click()
    time.sleep(10)