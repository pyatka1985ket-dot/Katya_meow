import pytest
from selenium import webdriver
import time
from pages.homepages import Homepages
from pages.product import ProductPage
from selenium.webdriver.firefox.options import Options


@pytest.fixture
def browser():
    options = Options()
    options.add_argument('--headless')
    browser = webdriver.Firefox(options=options)
    browser.maximize_window()
    browser.implicitly_wait(3)
    yield browser
    browser.close()



def test_open_s6(browser):
    homepages = Homepages(browser)
    homepages.open()
    homepages.click_galaxy_s6()
    product_page = ProductPage(browser)
    product_page.check_title_is('Samsung galaxy s6')




def test_two_monitors(browser):
    homepages = Homepages(browser)
    homepages.open()
    #browser.get('https://demoblaze.com/index.html')
    homepages.click_monitor()
    #monitors_link = browser.find_element(By.CSS_SELECTOR, value = '''[onclick="byCat('monitor')"]''')
    #monitors_link.click()
    time.sleep(2)  # позорище
    homepages.check_that_products_count(2)
    #monitors = browser.find_elements(By.CSS_SELECTOR, value = '.card')
    #assert len(monitors) == 2




