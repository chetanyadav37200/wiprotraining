import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope='module')
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    yield driver
    driver.quit()


def test_simple_alert(driver):
    driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
    alert=driver.switch_to.alert
    assert alert.text=="I am a JS Alert",'Alert text was weong'
    time.sleep(3)
    alert.accept()
    time.sleep(3)
    result=driver.find_element(By.ID,'result').text
    assert "You successfully clicked an alert" in result,'Result text was wrong'


def test_is_confirmdismiss(driver):
    driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
    alert = driver.switch_to.alert
    assert alert.text == "I am a JS Confirm", 'Alert text was weong'
    time.sleep(3)
    alert.dismiss()
    time.sleep(3)
    result = driver.find_element(By.ID, 'result').text
    assert "You clicked: cancel" in result, 'Result text was wrong'


def test_is_confirmdismissOK(driver):
    driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
    alert = driver.switch_to.alert
    assert alert.text == "I am a JS Confirm", 'Alert text was weong'
    time.sleep(3)
    alert.accept()
    time.sleep(3)
    result = driver.find_element(By.ID, 'result').text
    assert "You clicked: Ok" in result, 'Result text was wrong'



def test_is_prompt(driver):
    driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
    alert = driver.switch_to.alert
    assert alert.text == "I am a JS prompt", 'Alert text was wrong'
    alert.send_keys('Python Selenium')
    time.sleep(3)
    alert.accept()
    time.sleep(3)
    result = driver.find_element(By.ID, 'result').text
    assert "Python Selenium" in result, 'Result text was wrong'