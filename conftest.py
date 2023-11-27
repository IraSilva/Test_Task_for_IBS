import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def driver():
    print('\nstart browser...')
    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--start-maximized')
    driver = webdriver.Chrome(service=Service(), options=chrome_options)
    yield driver
    print('\nquit browser...')
    driver.quit()
