from behave import given, when, then
from selenium.common.exceptions import NoSuchElementException


@given('I have the list with the tuits')
def step_impl(context):
    br = context.browser
    br.find_element_by_id('id_screen_name').send_keys('rayato27')
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()

    br.find_element_by_id('search_button').click()

    assert br.find_element_by_id('word0')


@when('I press delete button')
def step_impl(context):

    br = context.browser
    print(br.page_source)
    br.find_element_by_id('delete_button').click()


@then('I do no￿t have the list with the tuits')
def step_impl(context):
    br = context.browser

    # check list is empty

    try:
        br.find_element_by_id('word0')
    except NoSuchElementException:
        return True
    return False
