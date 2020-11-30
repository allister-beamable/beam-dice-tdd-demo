from behave import given, when, then


@given('our dice rolling interface')
def dice_setup(context):
  assert context.client


@when('we ask to roll one die')
def request_roll(context):
  context.response = context.client.get('/dice')


@then('the total number should be between {low} and {high}')
def check_roll(context, low, high):
  total = context.response.json['total']
  assert int(low) <= total <= int(high)
