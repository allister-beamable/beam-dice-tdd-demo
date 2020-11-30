from behave import fixture, use_fixture
import beamdice


@fixture
def dice_client(context, *args, **kwargs):
  app = beamdice.create_app()
  app.testing = True
  context.client = app.test_client()
  yield context.client


def before_feature(context, feature):
  use_fixture(dice_client, context)
