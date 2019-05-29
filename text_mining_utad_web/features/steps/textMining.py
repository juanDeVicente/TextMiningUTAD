import pytest
from behave import given, when, then
from selenium.common.exceptions import NoSuchElementException


@given("I have not entered an user")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    br = context.browser
    assert br.find_element_by_id('id_screen_name').get_property('value') == ''


@given("I cant see the list with the tuits")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    br = context.browser
    with pytest.raises(Exception):
        br.find_element_by_id('word0')


@given('I have the list with the tuits')
def step_impl(context):
    br = context.browser
    # check list is not empty
    br.find_element_by_id('id_screen_name').send_keys('rayato27')
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()

    br.find_element_by_id('search_button').click()

    assert br.find_element_by_id('word0')


@when("I introduce an user")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.find_element_by_id('id_screen_name').send_keys('rayato27')


@when("I introduce a language")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.find_element_by_id('id_language').send_keys('Spanish')


@when("I press search button")
def step_impl(context):
    # Checks for Cross-Site Request Forgery protection input
    assert context.find_element_by_name('csrfmiddlewaretoken').is_enabled()
    context.find_element_by_id('search_button').click()


@then('I can see the list with the tuits')
def step_impl(context):
    # check list is not empty
    list_empty = context.find_element_by_id('word0')
    assert list_empty is not None


@when('I press delete button')
def step_impl(context):
    br = context.browser
    br.find_element_by_id('delete_button').click()


@then('I do not have the list with the tuits')
def step_impl(context):
    # check list is empty
    try:
        context.find_element_by_id('word0')
    except NoSuchElementException:
        return True
    return False