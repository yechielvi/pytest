# mypy: allow-untyped-defs
from __future__ import annotations

import pytest


@pytest.fixture
def xyzsomething(request):
    return 42


def test_func(some):
    pass
