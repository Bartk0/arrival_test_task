import json

import requests
from hamcrest import assert_that, equal_to


class BearTypes:
    BLACK = "BLACK"
    POLAR = "POLAR"
    BROWN = "BROWN"
    GUMMY = "GUMMY"


class BearHelper:
    def __init__(self, host=None, types=BearTypes):
        self.host = host
        self.path = "/".join([self.host, "bear"])
        self.types = types

    def delete_all(self):
        res = requests.delete(self.path)
        assert_that(res.status_code, equal_to(200))

    def delete(self, bear_id):
        res = requests.delete("/:".join([self.path, bear_id]))
        assert_that(res.status_code, equal_to(200))

    def create(self, bear_name="Misha", bear_type=BearTypes.GUMMY, bear_age=18.99):
        body = json.dumps({
            "bear_type": bear_type,
            "bear_name": bear_name,
            "bear_age": bear_age
        })
        res = requests.post(self.path, data=body)
        assert_that(res.status_code, equal_to(200))
        assert_that(res.headers.get("Content-type"), equal_to("text/html;charset=utf-8"))
        return res

    def read_all(self):
        res = requests.get(self.path)
        assert_that(res.status_code, equal_to(200))
        assert_that(res.headers.get("Content-type"), equal_to("text/html;charset=utf-8"))
        return res

    def read(self, bear_id):
        res = requests.get("/:".join([self.path, bear_id]))
        assert_that(res.status_code, equal_to(200))
        assert_that(res.headers.get("Content-type"), equal_to("text/html;charset=utf-8"))
        return res

    def update(self, bear_id, bear_name, bear_type, bear_age):
        body = json.dumps({
            "bear_type": bear_type,
            "bear_name": bear_name,
            "bear_age": bear_age
        })
        res = requests.put(":".join([self.path, bear_id]), data=body)
        assert_that(res.status_code, equal_to(200))
        return res

    def get_info(self):
        res = requests.get("/".join([self.host, "info"]))
        assert_that(res.status_code, equal_to(200))
        assert_that(res.headers.get("Content-type"), equal_to("text/html;charset=utf-8"))
        return res

    @staticmethod
    def assert_bear_data(bear_obj, ref_bear_id, ref_bear_name="Misha", ref_bear_type=BearTypes.GUMMY,
                         ref_bear_age=18.99):
        assert_that(bear_obj["bear_id"], equal_to(ref_bear_id))
        assert_that(bear_obj["bear_name"], equal_to(ref_bear_name))
        assert_that(bear_obj["bear_type"], equal_to(ref_bear_type))
        assert_that(bear_obj["bear_age"], equal_to(ref_bear_age))


class BearConsts:
    GOOD_INFO = 'Welcome to Alaska!\nThis is CRUD service for bears in alaska.\nCRUD routes presented with REST ' \
                'naming notation:\n\nPOST\t\t\t/bear - create\nGET\t\t\t/bear - read all bears\nGET\t\t\t/bear/:id ' \
                '- read specific bear\nPUT\t\t\t/bear/:id - update specific bear\nDELETE\t\t\t/bear - ' \
                'delete all bears\nDELETE\t\t\t/bear/:id - delete specific bear\n\n' \
                'Example of ber json: {"bear_type":"BLACK","bear_name":"mikhail","bear_age":17.5}.\n' \
                'Available types for bears are: POLAR, BROWN, BLACK and GUMMY.'
