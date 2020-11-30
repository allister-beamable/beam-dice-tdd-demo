from behave import fixture, use_fixture
from beamdice import app


@fixture
def dice_client(context, *args, **kwargs):
  app.testing = True
  context.client = app.test_client()
  yield context.client


def before_feature(context, feature):
  use_fixture(dice_client, context)
