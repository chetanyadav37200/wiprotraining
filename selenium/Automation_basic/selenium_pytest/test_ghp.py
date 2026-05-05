import time

from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import pytest_check as check


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://www.google.com/")
    yield driver
    driver.quit()

def test_ghploaded(driver):
    page_title = driver.title
    assert page_title == "Google", "Google Home Page Not Loaded"

def test_imagepageloaded(driver):
    driver.find_element(By.LINK_TEXT,'Images').click()
    pagetittle=driver.title
    assert pagetittle=='Google Images',"Image Page not found"

def test_Busspageloaded(driver):
    driver.find_element(By.LINK_TEXT, 'Business').click()

    wait = WebDriverWait(driver, 10)

    # Wait until URL contains "business"
    wait.until(EC.url_contains("business"))

    #pagetitle = driver.title
    time.sleep(3)
    #assert "Business Profile" in pagetitle, "Business Page not found"
    #assert "business" in driver.current_url.lower(), "Business page URL is not present"
    check.is_in(driver.title,'Business','Business page is not loaded')
    check.is_in(driver.current_url,'business','url not found')
