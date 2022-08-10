import time
from selenium.webdriver.common.by import By


def test_find_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(3)   #30 слишком много
    button = browser.find_element(By.CSS_SELECTOR, ".add-to-basket button")
    time.sleep(2)
    assert button is not None, "Button don't exists!"