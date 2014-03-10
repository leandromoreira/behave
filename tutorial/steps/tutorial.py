from behave import given
from behave import when
from behave import then
from hamcrest import assert_that
from hamcrest import equal_to

# code being tested
from sum import sum

@given(u'we a machine to sum two numbers')
def setup(context):
    context.sum_machine = sum.Sum()

@when(u'the first one is "{a}" and the second is "{b}"')
def when_first_and_second_numbers_are(context, a, b):
    context.result = context.sum_machine.sum(int(a), int(b))

@then(u'the sum is "{result}"!')
def we_sum(context, result):
    assert_that(context.result, equal_to(int(result)))
