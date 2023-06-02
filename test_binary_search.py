import pytest

from binary_search import binary_search


@pytest.mark.parametrize(
    ("numbers", "find", "result"),
    [
        ([1, 2, 3], 2, True),
        ([9, 11], 5, False),
        (
            [
                1,
                2,
                3,
                8,
                11,
                14,
                15,
                19,
                220,
                7684,
                241905,
                438609,
                12501208,
                25930251242,
                2105012432432,
                5906403295032,
            ],
            25930251242,
            True,
        ),
        (
            [
                1,
                2,
                3,
                8,
                11,
                14,
                15,
                19,
                220,
                7684,
                241905,
                438609,
                12501208,
                25930251242,
                2105012432432,
                5906403295032,
            ],
            5906403295032555,
            False,
        ),
    ],
)
def test_binary_search_success(numbers, find, result):
    assert binary_search(numbers, find) == result
