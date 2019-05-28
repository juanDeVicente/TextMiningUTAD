from selenium import webdriver

# FUNCTIONS USED ON THE  SELENIUM TESTS
from selenium.common.exceptions import WebDriverException


def got_to_web():
    from selenium.webdriver.firefox.options import Options
    driver = webdriver.Firefox()
    driver.get('http://localhost:8000')
    return driver


def list_is_not_empty(context):
    try:
        context.find_element_by_id('word0')
        return True
    except:
        return False


def textboxt_empty(context):
    try:
        return context.find_element_by_id('username').get_property('value') == ''
    except:
        return False
