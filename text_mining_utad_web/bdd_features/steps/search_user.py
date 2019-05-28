from behave import given, when, then


# user exists
@given('I have entered an user')
def step_impl(context):

    # set the ￿￿'@' of the user we want to search
    u = '@rayato27'


@when("I press search button")
def step_impl(context):

    br = context.browser

    # Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()

    # Fill login form and submit it (valid version)
    br.find_element_by_name('id_screen_name').send_keys('u')
    br.find_element_by_name('search_button').click()


@then('I can see the list with the tuits')
def step_impl(context):
    br = context.browser

    # check list is empty
    list_empty = context.find_element_by_id('word0')

    if list_empty is True:
        return True
    else:
        return False


