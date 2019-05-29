from selenium import webdriver


def before_all(context):
    # For debugging purposes, you can use the Firefox driver instead.
    context = webdriver.Firefox()
    context.implicitly_wait(1)
    context.get('http://localhost:8000')
    context.implicitly_wait(1)


def after_all(context):
    # Explicitly quits the browser, otherwise it won't once tests are done
    context.browser.quit()


def before_feature(context, feature):
    # Code to be executed each time a feature is going to be tested
    pass