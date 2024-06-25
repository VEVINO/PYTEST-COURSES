import os

import pytest

QA_config = 'qa.prop'
prod_config = 'prod.prop'


def pytest_addoption(parser):
    parser.addoption("--cmdopt", default='QA')


@pytest.fixture()
def CmdOpt(pytestconfig):
    print("\n In CmdOpt fixtures function")
    opt = pytestconfig.getoption("cmdopt")
    if opt == 'Prod':
        f = open(os.path.join(os.path.dirname(__file__), prod_config), 'r')
    else:
        f = open(os.path.join(os.path.dirname(__file__), QA_config), 'r')
        yield f

# command argumend from the command line