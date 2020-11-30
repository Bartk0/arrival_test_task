import random

import allure
from hamcrest import assert_that, equal_to

from helpers.bears import BearTypes
from helpers.test_data import random_string


@allure.testcase('Read by id', name="Test of reading info about specific bear")
@allure.description("Create and read bear by id")
def test_read_by_id(bears):
    with allure.step('create bear'):
        create_result = bears.create()
        bear_id = create_result.text

    with allure.step('read bear info with id'):
        read_result = bears.read(bear_id)
        bears.assert_bear_data(read_result.json(), bear_id)

    with allure.step('delete all bears'):
        bears.delete(bear_id)

    with allure.step('read bear info with id'):
        read_result = bears.read(bear_id)
        assert_that(read_result.text, equal_to("EMPTY"))


@allure.testcase('Read all', name="Test of reading all the bears")
@allure.description("Create, read and delete")
def test_read_all(bears):
    with allure.step('create bears'):
        created_bears = {}
        bears_count = 10
        for i in range(bears_count):
            bear_name = random_string("bear", 10)
            bear_type = [BearTypes.POLAR, BearTypes.GUMMY, BearTypes.BLACK, BearTypes.BROWN][random.randrange(3)]
            bear_age = random.randrange(-100, 100)
            create_result = bears.create(bear_name, bear_type, bear_age)
            created_bears.update({create_result.text: {
                "bear_type": bear_type,
                "bear_name": bear_name,
                "bear_age": bear_age
            }})

    with allure.step('read bear info with ids'):
        read_result = bears.read_all().json()
        bears_info_ids = created_bears.keys()
        for bear in read_result:
            bear_id = str(bear["bear_id"])
            if bear_id in bears_info_ids:
                created_bear_info = created_bears[bear_id]
                bears.assert_bear_data(bear, int(bear_id), created_bear_info["bear_name"],
                                       created_bear_info["bear_type"], created_bear_info["bear_age"])
                created_bears.pop(bear_id)
        if not len(created_bears) == 0:
            raise AssertionError(f"{len(created_bears)} Bears escaped!")

    with allure.step('delete all bears'):
        bears.delete_all()

    with allure.step('read bears info'):
        read_result = bears.read_all()
        assert_that(read_result.text, equal_to("[]"))
