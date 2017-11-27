from fip.fip import Fip
import pytest


@pytest.fixture()
def fip():
    return Fip()
