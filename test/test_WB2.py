import pytest
import selenium
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC



def test_open_wb2(browser):
    options = Options()
    options.add_argument('--headless')
    browser.get('https://career.rwb.ru/?/index.html')
    time.sleep(2)
    vacancy = browser.find_element(By.CSS_SELECTOR, "a[href='/vacancies']")
    browser.execute_script("arguments[0].click();", vacancy)
    time.sleep(3)
    title = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'h2'))
        )
    assert title.text == 'Присоединяйся к команде'