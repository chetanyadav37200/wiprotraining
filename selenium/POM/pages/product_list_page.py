import time
from operator import truediv

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductListPage:
    PRODUCT_TITLE=(By.CSS_SELECTOR,'a h2 span')
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver,10)



    def find_product_title(self,brandname):
        first_product=self.wait.until(EC.visibility_of_element_located(self.PRODUCT_TITLE))
        print("\nFirst Product:",first_product.text)

    def all_products(self):
        product_titles = self.wait.until(
            EC.presence_of_all_elements_located(self.PRODUCT_TITLE)
        )
        print(f"\nFound {len(product_titles)}")
        for i, title in enumerate(product_titles[:5], start=1):
            print(f"{i}. {title.text}")
        return len(product_titles)>0  # return the list

    from selenium.webdriver.common.by import By

    def brand_filter_locator(self, brandname):
        BRAND_FILTER = (By.XPATH, "//span[text()='" + brandname + "']/parent::a/descendant::i")
        return BRAND_FILTER

    def select_brand_filter(self, brandname):
        brand_filter = self.driver.find_element(*self.brand_filter_locator(brandname))
        brand_filter.click()
        time.sleep(5)

    def check_product_titles_for_brand_filter(self, brandname):
        product_titles = self.wait.until(EC.presence_of_all_elements_located(self.PRODUCT_TITLE))
        for title in product_titles:
            print("\ntitle  HELLO :", title.text)
            if brandname.lower() not in title.text.lower():
                return False
        return True

    def mens_size_locator(self,menssize):
        MENSIZE_FILTER= (By.XPATH,"(//span[@class='a-list-item']/descendant::button[@value'"+menssize +"'])[1] " )
        return MENSIZE_FILTER

    def select_menssize_filter(self,menssize):
        menssize_filter= self.driver.find_element(*self.mens_size_locator(menssize))
        menssize_filter.click()

    def check_size(self,menssize):
        return menssize in self.driver.title
