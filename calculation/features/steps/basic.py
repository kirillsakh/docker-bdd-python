"""
This module contains step definitions for basic.feature.
It uses Selenium WebDriver for browser interactions:
https://www.seleniumhq.org/projects/webdriver/
Setup and cleanup are handled in environment.py
"""

import os
from behave import *
from testutil import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

# Givens

@given('you set game url')
def step_impl(context):
	global GAME_URL
	HEADER = 'file://'
	absFilePath = os.path.abspath(__file__)
	fileDir = os.path.dirname(os.path.abspath(__file__))
	parentDir_up_1_level = os.path.dirname(fileDir)
	parentDir_up_2_level = os.path.dirname(parentDir_up_1_level)
	GAME_URL = HEADER + str(os.path.join(parentDir_up_2_level, 'index.html'))
	assert len(GAME_URL) > len(HEADER)

@given('game is ready')
def step_impl(context):
	context.browser.get(GAME_URL)
	assert "Addition and subtraction" in context.browser.title

# Whens

@when('you give "{answer_type}" answer')
def step_impl(context, answer_type):
	result = None
	isCorrect = False
	if answer_type == 'correct':
		isCorrect = True
	a = int(get_attribute_by_id(context.browser, 'a','value'))
	b = int(get_attribute_by_id(context.browser, 'b','value'))
	sign = get_attribute_by_id(context.browser, 'operator','innerHTML')
	if sign == '+':
		if isCorrect:
			result = a + b
	else:
		if isCorrect:
			result = a - b
	result_object = context.browser.find_element_by_id('r')
	result_object.send_keys(str(result)+Keys.RETURN)

# Thens

@then('"{image_type}" image is shown')
def step_impl(context, image_type):
	wait = WebDriverWait(context.browser, 1)
	assert wait.until(element_has_css_style((By.ID, image_type), "inline"))
	time.sleep(5)

