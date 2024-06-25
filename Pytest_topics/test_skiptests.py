import sys

import pytest

pytestmark = pytest.mark.skipif(sys.platform != 'win32', reason="will run only on window 32 os")

const = 9 / 5


def cent_tp_fah(cent=0):
    fah = (cent * const) + 32
    return fah


#print(cent_tp_fah())
@pytest.mark.skip(reason="Skiping for no reason specified")
def test_case01():
    assert type(const) == float


#@pytest.mark.skipif(sys.version_info < (3, 8), reason="doesnot work on py version above 3.6")
#@pytest.mark.skipif(cent_tp_fah()==32, reason="default value test, so skipping")
def test_case02():
    assert cent_tp_fah() == 32


@pytest.mark.skipif(pytest.__version__ < '8.2.0', reason="pytest version is less")
def testcase03():
    assert cent_tp_fah(38) == 100.4
