import pytest

from super_module import super_sum


@pytest.mark.parametrize("cond, exp", [
    ((1, 2), 3),
    ((-1, 2), 1),
    ((0, -1), -1),
    ((2, 0), 2)
])
def test_positive1(cond, exp):
    assert super_sum(cond[0], cond[1]) == exp
