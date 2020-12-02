import allure
from hamcrest import assert_that, equal_to, is_not

from helpers.bears import BearConsts


@allure.testcase('Info', name="Requests info about application")
@allure.description("Requests info about application, asserting with reference info")
def test_info(bears):
    result = bears.get_info()
    assert_that(result.text, is_not(None))
    assert_that(result.text, equal_to(BearConsts.GOOD_INFO))
    assert_that(result.headers.get("Content-type"), equal_to("text/html;charset=utf-8"))
