from selenium import webdriver


def before_all(context):
    try:
        context.browser = webdriver.Firefox()
    except Exception:
        print('hola')
    context.browser.implicitly_wait(1)
    context.browser.get('http://localhost:8000')


def after_all(context):
    # Explicitly quits the browser, otherwise it won't once tests are done

    context.browser.quit()


def before_feature(context, feature):
    # Code to be executed each time a feature is going to be tested
    if feature.name == 'Delete button':
        br = context.browser
        # set the ￿￿'@' of the user we want to search
        br.find_element_by_id('search_button').click()
