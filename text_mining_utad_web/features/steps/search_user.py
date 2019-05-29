import pytest
from behave import given, when, then


@given("I have not entered an user")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    br = context.browser
    print(br.page_source)
    assert br.find_element_by_id('id_screen_name').get_property('value') == ''


@given("I cant see the list with the tuits")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    br = context.browser
    with pytest.raises(Exception):
        br.find_element_by_id('word0')


@when("I introduce an user")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    br = context.browser
    br.find_element_by_id('id_screen_name').send_keys('rayato27')


@when("I introduce a language")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    br = context.browser
    br.find_element_by_id('id_language').send_keys('Spanish')


@when("I press search button")
def step_impl(context):

    br = context.browser
    # Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()

    br.find_element_by_id('search_button').click()


@then('I can see the list with the tuits')
def step_impl(context):
    br = context.browser

    # check list is not empty
    list_empty = br.find_element_by_id('word0')
    assert list_empty is not None
