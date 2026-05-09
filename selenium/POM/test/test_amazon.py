from pages.home_page import HomePage
from pages.product_list_page import ProductListPage

import pytest
def test_open_amazon(driver):
    assert "amazon" in driver.current_url, 'URL for Amazon is not correct'
    print("\nOpened Amazon")
@pytest.mark.parametrize("searchproduct",[
    ("wireless mouse"),('shoes')
])
def test_search_product(driver,searchproduct):
    homepage = HomePage(driver)
    homepage.type_search_input(searchproduct)
    print(f"Searchinf product - {searchproduct}")
    homepage.click_search_input()

    assert homepage.is_amazon_page_loaded()
    print("\nSearch result page loaded successfully -",searchproduct)



@pytest.mark.parametrize("searchproduct",[
    ("wireless mouse"),('shoes')
])

def test_find_element_amazon(driver,searchproduct):

    homepage = HomePage(driver)

    homepage.type_search_input(searchproduct)
    print(f"Searchinf product - {searchproduct}")
    homepage.click_search_input()

    assert homepage.is_amazon_page_loaded()
    print("\nSearch result page loaded successfully -",searchproduct)

    productlistingpage = ProductListPage(driver)

    productlistingpage.find_product_title()
    val = productlistingpage.all_products()

    assert val,"NO products found on amazon search result"


@pytest.mark.parametrize(("searchproduct", "brandname"),[
    ("wireless mouse",'Logitech'),('shoes','Nike')
])
def test_brand_filter(driver, searchproduct, brandname ):
    homepage = HomePage(driver)

    homepage.type_search_input(searchproduct)
    print(f"Searching product - {searchproduct}")
    homepage.click_search_input()

    assert homepage.is_amazon_page_loaded()
    print("\nSearch result page loaded successfully -", searchproduct)

    productlistpage = ProductListPage(driver)

    productlistpage.select_brand_filter()
    assert productlistpage.check_product_titles_for_brand_filter(brandname),"Brand "




@pytest.mark.parametrize(("searchproduct", "brandname" , "menssize"),[
    ('shoes','Nike','9')
])
def test_product_odering(driver,searchproduct,brandname,menssize):
    homepage = HomePage(driver)

    homepage.type_search_input(searchproduct)
    print(f"Searching product - {searchproduct}")
    homepage.click_search_input()

    assert homepage.is_amazon_page_loaded()
    print("\nSearch result page loaded successfully -", searchproduct)

    productlistingpage = ProductListPage(driver)

    productlistingpage.find_product_title(brandname)

    assert productlistingpage.check_product_titles_for_brand_filter(brandname), "Brand fillter didi no apply"

    productlistingpage.select_menssize_filter(menssize)

    assert productlistingpage.check_size(menssize), "Brand fillter didi no apply"
