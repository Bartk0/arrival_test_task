import allure

from helpers.bears import BearTypes


@allure.testcase('Update', name="Test of bear updating")
@allure.description("Create, update and delete")
def test_update(bears):
    with allure.step('create bear'):
        create_result = bears.create()
        bear_id = create_result.text

    with allure.step('read bear info with id'):
        read_result = bears.read(bear_id)
        bears.assert_bear_data(read_result.json())

    with allure.step('update bear'):
        new_name = "Broken teeth"
        new_type = BearTypes.POLAR
        new_age = 34
        bears.update(bear_id, new_name, new_type, new_age)

    with allure.step('read updated bear info'):
        read_result = bears.read(bear_id)
        bears.assert_bear_data(read_result.json(), bear_id, new_name, new_type, new_age)

    with allure.step('delete all bears'):
        bears.delete_all()
