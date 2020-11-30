from behave import *
import requests


@given('our dice rolling interface')
def step_impl(context):
  context.url = 'http://localhost:9000/'


@when('we ask to roll one die')
def step_impl(context):
  context.response = requests.get(context.url)


@then('the total number should be between {low} and {high}')
def step_impl(context, low, high):
  total = context.response.json()['total']
  assert low <= total <= high
