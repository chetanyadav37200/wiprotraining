import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Edge()
driver.maximize_window()
driver.get("https://www.selenium.dev/selenium/web/web-form.html")
time.sleep(1)

text_input=driver.find_element(By.ID,'my-text-id')
text_input.clear()
text_input.send_keys("selenium webdriver demo")

password_input=driver.find_element(By.NAME,'my-password')
password_input.clear()
password_input.send_keys('secret123')

textarea_input=driver.find_element(By.NAME,"my-textarea")
textarea_input.clear()
textarea_input.send_keys("Selenium with python")


check_click=driver.find_element(By.ID,"my-check-1")
check_click.click()

check_click2=driver.find_element(By.ID,"my-check-2")
check_click2.click()

radio_click=driver.find_element(By.ID,"my-radio-2")
radio_click.click()

drop_sele=driver.find_element(By.NAME,'my-select')
drop_sele.click()
option=driver.find_element(By.CSS_SELECTOR,"select[name='my-select'] option[value='2']")
option.click()

multi_sele=driver.find_element(By.NAME,'my-datalist')
multi_sele.send_keys('New York')

file_upload=driver.find_element(By.NAME,'my-file')
file_upload.send_keys(r"C:\Wipro Training\python\first")

range_slider=driver.find_element(By.NAME,'my-range')
driver.execute_script("arguments[0].value = 10;", range_slider)

date_input=driver.find_element(By.NAME,'my-date')
date_input.send_keys('12/05/2025')

color_input = driver.find_element(By.NAME, 'my-colors')
color_input.send_keys('#00ff00')
sumit_btn=driver.find_element(By.CSS_SELECTOR,"button[type='submit']")
sumit_btn.click()
time.sleep(10)