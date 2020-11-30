from behave import given, when, then

MANY = 100


@given('the dice roller is set up')
def dice_setup(context):
  assert context.client


@when('we roll one die')
def request_roll(context):
  context.response = context.client.get('/dice')


@when('we roll a bunch of times')
def request_many_rolls(context):
  context.responses = []
  for _ in range(MANY):
    context.execute_steps('when we roll one die')
    context.responses.append(context.response)


@then('the total number should be between {low} and {high}')
def check_roll(context, low, high):
  total = context.response.json['total']
  assert int(low) <= total <= int(high)


@then('eventually the number should be something other than {number}')
def check_many_rolls(context, number):
  avoided_number = int(number)
  same = True
  for response in context.responses:
    total = response.json['total']
    if total != avoided_number:
      same = False
  assert not same


@then('eventually {number} should appear')
def check_value_distribution(context, number):
  expected_number = int(number)
  observed = False
  for response in context.responses:
    total = response.json['total']
    if total == expected_number:
      observed = True
  assert observed
