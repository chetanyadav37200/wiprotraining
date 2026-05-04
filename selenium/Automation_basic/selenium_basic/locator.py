import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service
from selenium.webdriver.support.relative_locator import locate_with

driver=webdriver.Edge(service=Service("../resource/msedgedriver.exe"))


'''searh_input=driver.find_element(By.ID,"APjFqb")
searh_input.send_keys("selenium")
time.sleep(3)
searh_input.clear()
'''
#name
'''search_input=driver.find_element(By.NAME,'q')
search_input.send_keys("Locators")
time.sleep(3)'''

#name
'''googlesearch_button=driver.find_element(By.NAME,'btnK')
googlesearch_button.click()
time.sleep(40)
driver.quit()'''

#classname
'''imfl_button=driver.find_element(By.CLASS_NAME,"RNmpXc")
imfl_button.click()
time.sleep(3)'''

#tagname
'''href_elements = driver.find_elements(By.PARTIAL_LINK_TEXT, 'ma')
for element in href_elements:
    print(f"{element.text} - {element.get_attribute('href')}")'''

#css selector
'''search_input=driver.find_element(By.CSS_SELECTOR,'div>textarea')
search_input.send_keys("selenium")
time.sleep(3)
search_input.clear()
driver.quit()

'''
#driver.get("https://the-internet.herokuapp.com/tables")

'''# AND example
and_example = driver.find_element(By.XPATH,"//td[text()='Tim' and @class='first-name']")
print(f"And Example -. Found with both condition : {and_example.text}")

# OR example
or_example = driver.find_element(By.XPATH,"//td[text()='Tim' or text()='Frank']")
print(f"OR Example -. Found with both condition : {or_example.text}")

# Count columns in first row
first_row = driver.find_element(By.XPATH,"//table[@id='table1']/tbody/tr[1]")
columns = first_row.find_elements(By.TAG_NAME,"td")
print(f"Child Example -> Found {len(columns)} columns in the first row")

# Parent example
email_cell = driver.find_element(By.XPATH,"//table[@id='table1']//td[text()='jdoe@hotmail.com']")
parent_row = email_cell.find_element(By.XPATH,"./parent::tr")
print(f"Parent Example -> Email '{email_cell.text}' belongs to row with first name: "
      f"{parent_row.find_element(By.XPATH,'./td[2]').text}")
'''
'''# Ancestor
ancestor_table = driver.find_element(By.XPATH,"//td[text()='jsmith@gmail.com']/ancestor::table")
print(f"Ancestor Example -> Table ID: {ancestor_table.get_attribute('id')}")

# Descendant
descendants = driver.find_elements(By.XPATH,"//table[@id='table1']/descendant::td")
print(f"Descendant Example -> found {len(descendants)} descendant cells")
'''
driver.get('https://www.saucedemo.com/')
time.sleep(2)

#element used for reference
username_field=driver.find_element(By.ID,'user-name')
password_field=driver.find_element(By.ID,'password')
login_button=driver.find_element(By.ID,'login-button')

#above element
elst_above_password=driver.find_element(
    locate_with(By.TAG_NAME,"input").above(password_field)
)
print(f"Above Example->Text Above password: {elst_above_password.get_attribute('placeholder')}")
elst_above_password.send_keys('standard_user')
time.sleep(5)

#below element
elst_below_username=driver.find_element(
    locate_with(By.TAG_NAME,"input").below(username_field)
)
print(f"Below Example->placeholder below username: {elst_below_username.get_attribute('placeholder')}")
elst_below_username.send_keys('secret_sauce')
time.sleep(2)
login_button.click()
time.sleep(3)

twwiter_icon=driver.find_element(By.LINK_TEXT,'Twitter')
facebook_icon=driver.find_element(locate_with(By.TAG_NAME,'a').to_right_of(twwiter_icon))
print(f"toRight Example-> Element to the right of twitter icon has href:{facebook_icon.get_attribute('href')}")

left_icon=driver.find_element(locate_with(By.TAG_NAME,'a').to_left_of(facebook_icon))
print(f"toleft Example-> Element to the left of facebook icon has href:{left_icon.get_attribute('href')}")

near_facebook=driver.find_elements(locate_with(By.TAG_NAME,'a').near(facebook_icon))
for element in near_facebook:
    print(f"Near Exampke near Facebook icon has: {element.get_attribute('href')}")
time.sleep(3)
driver.quit()
