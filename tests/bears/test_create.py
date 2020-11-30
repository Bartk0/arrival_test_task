import allure
import pytest

from helpers.test_data import bears_generator

test_data = bears_generator(20)


def case_data(bear_name):
    return bear_name


@allure.testcase('Create', name="Test of create method")
@allure.description("Create and read")
@pytest.mark.parametrize("bear_name, bear_type, bear_age", test_data, ids=case_data)
def test_create(bears, bear_name, bear_type, bear_age):
    with allure.step('create bear'):
        create_result = bears.create(bear_name, bear_type, bear_age)
        bear_id = create_result.text

    with allure.step('read bear info with id'):
        read_result = bears.read(bear_id)
        bears.assert_bear_data(read_result.json(), bear_name, bear_type, bear_age)

    with allure.step('read all bears'):
        read_result = bears.read_all()
        result_data = read_result.json()
        for bear in result_data:
            if bear["bear_id"] == int(bear_id):
                bears.assert_bear_data(bear, bear_id, bear_name, bear_type, bear_age)

