## Author: Stephen Mugisha
## Test algorithm solutions

import pytest
from remove_duplicates_from_sorted_array import removeDuplicates


def test_pass():
    """Assert the test passes"""
    assert True


@pytest.fixture
def dups_data():
    return [
        [0,0,1,1,1,1,2,3,3],
        [1,1,1,2,2,3],
        [2,2,2,2,2,3]
    ]

def test_removeDuplicates(dups_data):
    assert removeDuplicates(dups_data[0]) == 7
    assert removeDuplicates(dups_data[1]) == 5

def test_failremoveDuplicates(dups_data):
    assert removeDuplicates(dups_data[2]) != 2

