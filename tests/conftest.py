from os import path

import pytest
from vyper import v

from helpers.bears import BearHelper

ROOT_DIR = path.join(path.dirname(path.abspath(__file__)), '..')


def setup_config():
    v.set_config_name('config')
    v.set_config_type('yaml')
    v.add_config_path(ROOT_DIR)
    v.read_in_config()


@pytest.fixture(scope='session', autouse=True)
def init():
    setup_config()


@pytest.fixture(scope='session')
def bears():
    return BearHelper(v.get('bears.host'))
