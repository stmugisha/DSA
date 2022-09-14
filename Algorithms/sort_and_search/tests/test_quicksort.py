## Quick sort tests
## Author: Stephen Mugisha

import pytest
from sorting import quicksort as qst

def test_pass():
    assert True

#def test_fails():
#    assert False

@pytest.fixture
def quick_sort_data():
    return [
        [13,5,3,1,7,11,9],
        [6,2,4,0,8,12,10]
    ]

def test_quicksort(quick_sort_data):
    assert qst.quicksort(quick_sort_data[0]) == sorted(quick_sort_data[0])
    assert qst.quicksort(quick_sort_data[1]) == sorted(quick_sort_data[1])



