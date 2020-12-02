import allure
from hamcrest import assert_that, equal_to, is_not


@allure.testcase('Delete by id', name="Test of deleting specific bears")
@allure.description("Create, read and delete")
def test_delete_by_id(bears):
    with allure.step('create bear'):
        create_result = bears.create()
        bear_id = create_result.text

    with allure.step('read bear info with id'):
        read_result = bears.read(bear_id).json()
        assert_that(read_result, is_not(None))
        bears.assert_bear_data(read_result, bear_id)

    with allure.step('delete bear'):
        bears.delete(bear_id)

    with allure.step('read bear info with id'):
        read_result = bears.read(bear_id).text
        assert_that(read_result, is_not(None))
        assert_that(read_result, equal_to("EMPTY"))


@allure.testcase('Delete all', name="Test of deleting all bears")
@allure.description("Create, read and delete")
def test_delete_all(bears):
    with allure.step('create 10 bears'):
        for i in range(10):
            bears.create()

    with allure.step('check for bears creation'):
        read_result = bears.read_all().text
        assert_that(read_result, is_not(None))
        assert_that(read_result, is_not(equal_to("[]")))

    with allure.step('delete all bears'):
        bears.delete_all()

    with allure.step('read bear info with id'):
        read_result = bears.read_all().text
        assert_that(read_result, is_not(None))
        assert_that(read_result, equal_to("[]"))
