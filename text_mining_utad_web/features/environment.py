from selenium import webdriver


def before_all(context):
    # For debugging purposes, you can use the Firefox driver instead.
    context.browser = webdriver.Firefox()
    context.browser.implicitly_wait(1)
    context.server_url = 'http://localhost:8000'
    context.browser.get(context.server_url)
    context.browser.implicitly_wait(1)


def after_all(context):
    # Explicitly quits the browser, otherwise it won't once tests are done
    context.quit()


def before_feature(context, feature):
    # Code to be executed each time a feature is going to be tested
    pass
