from behave import given, when, then


@given('our dice rolling interface')
def step_impl(context):
  assert context.client


@when('we ask to roll one die')
def step_impl(context):
  context.response = context.client.get('/dice')


@then('the total number should be between {low} and {high}')
def step_impl(context, low, high):
  total = context.response.json()['total']
  assert low <= total <= high
