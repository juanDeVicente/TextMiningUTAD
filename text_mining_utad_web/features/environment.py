import os

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


def before_all(context):
    try:
        context.browser = webdriver.Firefox()
    except Exception as e:
        print(os.environ['PATH'])
        print(e)
    context.browser.implicitly_wait(1)
    context.browser.get('http://localhost:8000')


def after_all(context):

    # Explicitly quits the browser, otherwise it won't once tests are done

    context.browser.quit()


def before_feature(context, feature):
    # Code to be executed each time a feature is going to be tested
    pass
