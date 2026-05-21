import pytest
import selenium
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC


def test_open_wb(browser):
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


def test_header(browser):
    options = Options()
    options.add_argument('--headless')
    browser.get('https://career.rwb.ru/?/index.html')
    all_vacancy = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Все вакансии"))
    )
    assert all_vacancy.text == 'Все вакансии'
    team_link=WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[data-qa='header-btn-/start']"))
        )
    assert team_link.text == 'Попасть в команду'
    intern_link = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[data-qa='header-btn-/intern']"))
    )
    assert intern_link.text == 'Без опыта'
    construction_link = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[data-qa='header-btn-/construction']"))
    )
    assert construction_link.text == 'Строительство'
    service_link = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='https://job.wb.ru/?utm_source=wb&utm_medium=career&utm_campaign=header']"))
    )
    assert service_link.text == 'Сервисные позиции'







