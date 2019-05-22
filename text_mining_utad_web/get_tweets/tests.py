#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.test import TestCase
import time
from text_mining_utad_web.get_tweets.functions_tests import *
from selenium.webdriver.common.keys import Keys



def test_textbox_using_enter():
    context = got_to_web()
    textbox = context.find_element_by_id("username")
    textbox.send_keys('perezreverte')
    language_button = context.find_element_by_id("language_id")
    language_button.send_keys('spanish')
    textbox.send_keys(Keys.ENTER)
    time.sleep(4)
    assert list_is_not_empty(context)


def test_username_exists_execute_button():
    context = got_to_web()
    textbox = context.find_element_by_id("username")
    textbox.send_keys('perezreverte')
    language_button = context.find_element_by_id("language_id")
    language_button.send_keys('spanish')
    button = context.find_element_by_id("button_execute")
    button.click()
    time.sleep(2)
    assert list_is_not_empty(context)


def test_username_not_exists_execute_button():
    context = got_to_web()
    textbox = context.find_element_by_id("username")
    textbox.send_keys('noestiejejdlfodjlkhx')
    language_button = context.find_element_by_id("language_id")
    language_button.send_keys('spanish')
    button = context.find_element_by_id("button_execute")
    button.click()
    assert list_is_not_empty(context) == False


def test_delete_button_filled_textbox():
    context = got_to_web()
    textbox = context.find_element_by_id("username")
    textbox.send_keys('perezreverte')
    language_button = context.find_element_by_id("language_id")
    language_button.send_keys('spanish')
    button = context.find_element_by_id("button_delete")
    button.click()
    time.sleep(2)
    assert textboxt_empty(context)


def test_delete_button_filled_list():
    context = got_to_web()
    textbox = context.find_element_by_id("username")
    textbox.send_keys('perezreverte')
    language_button = context.find_element_by_id("language_id")
    language_button.send_keys('spanish')
    button = context.find_element_by_id("button_execute")
    button.click()
    time.sleep(5)
    button2 = context.find_element_by_id("button_delete")
    button2.click()
    time.sleep(2)
    assert list_is_not_empty(context)


def test_empty_list_when_introduce_non_exist_twitter():
    context = got_to_web()
    textbox = context.find_element_by_id("username")
    textbox.send_keys('perezreverte')
    language_button = context.find_element_by_id("language_id")
    language_button.send_keys('spanish')
    button = context.find_element_by_id("button_execute")
    button.click()
    time.sleep(5)
    textbox.send_keys('noestiejejdlfodjlkhx')
    button.click()
    time.sleep(2)
    assert list_is_not_empty(context)


# USUARIO PRIVADO

# USUARIO SIN PONER IDIOMA