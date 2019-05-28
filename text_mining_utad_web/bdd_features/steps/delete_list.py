from behave import given, when, then


@given('I have the list with the tuits')
def step_impl(context):
    br = context.browser

    # check list is not empty
    assert br.find_element_by_id('word0')


@when('I press delete button')
def step_impl(context):

    br = context.browser

    # Fill login form and submit it (valid version)
    br.find_element_by_name('delete_button').click()


@then('I do no￿t have the list with the tuits')
def step_impl(context):
    br = context.browser

    # check list is empty
    list_empty = context.find_element_by_id('word0')

    if list_empty is False:
        return True
    else:
        return False
