from pytest_bdd import scenarios, parsers, given, when, then
from cucumbers import CucumberBasket


scenarios('../features/cucumbers.feature')

# Dictionary for converting value types
EXTRA_TYPES = {
    'Number': int
}


@given(parsers.cfparse('the basket has "{initial:Number}" cucumbers', extra_types=EXTRA_TYPES), target_fixture='basket')
def basket(initial):
    return CucumberBasket(initial_count=2)


@when(parsers.cfparse('"{some:Number}" cucumbers are added to the basket', extra_types=EXTRA_TYPES))
def add_cucumbers(basket, some):
    basket.add(some)


@then(parsers.cfparse('the basket contains "{total:Number}" cucumbers', extra_types=EXTRA_TYPES))
def basket_has_total(basket, total):
    assert basket.count == total
