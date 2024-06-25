import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
test_name = "Madrid"

opts=webdriver.ChromeOptions()
opts.add_argument("--headless")
opts.add_argument("--no-sanbox")
#opts.add_argument("--disable-dev-shm-usage")
driver=webdriver.Chrome(options=opts)
url="http://172.31.19.107"
def test_http():
    response = requests.get(url)
    assert response.status_code == 200

def test_location():
    driver.get(url)
    elem_input = driver.find_element(By.ID, "input")
    elem_input.send_keys(test_name)
    submit_elem = driver.find_element(By.CLASS_NAME, "button")
    submit_elem.click()
    header_elem = driver.find_element(By.CLASS_NAME, "location")
    assert test_name == header_elem.text

def test_location_negetive():
    driver.get(url)
    elem_input = driver.find_element(By.ID, "input")
    elem_input.send_keys("bla")
    submit_elem = driver.find_element(By.CLASS_NAME, "button")
    submit_elem.click()
    elem_week = driver.find_elements(By.XPATH, "/html/body/div/div/div[2]")
    assert elem_week == []



#     response = requests.get()
#     assert ("Python", driver)
