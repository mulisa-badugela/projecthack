from projecthack import recursion
from projecthack import sorting


def test_sum_array():
    """
    make sure top_n works correctly
    """

    assert myFunction.sum_array([1,1,1,1,1]) == 5, 'incorrect'
    assert myFunction.sum_array([5, 5, 10]) == 20, 'incorrect'

def test_fibonacci():

    assert myFunction.fibonacci(0) == 0, 'incorrect'
    assert myFunction.fibonacci(8) == 21, 'incorrect'


def test_factorial():

    assert myFunction.factorial(5) == 120, 'incorrect'
    assert myFunction.factorial(2) == 2, 'incorrect'

def test_reverse():

    assert myFunction.reverse('cook') == 'kooc', 'incorrect'
    assert myFunction.reverse('hello') == 'olleh', 'incorrect'


def test_bubble_sort():

    assert myFunction.bubble_sort([2,3,1,4,6,5]) == [1,2,3,4,5,6], 'incorrect'
    assert myFunction.bubble_sort([5,6,3,9,2,8,13,0]) == [0, 2, 3, 5, 6, 8, 9, 13], 'incorrect'

def test_merge_sort():

    assert myFunction.merge_sort([2,3,1,4,6,5]) == [1,2,3,4,5,6], 'incorrect'
    assert myFunction.merge_sort([5,6,3,9,2,8,13,0]) == [0, 2, 3, 5, 6, 8, 9, 13], 'incorrect'

def test_quick_sort():

    assert myFunction.quick_sort([2,3,1,4,6,5]) == [1,2,3,4,5,6], 'incorrect'
    assert myFunction.quick_sort([5,6,3,9,2,8,13,0]) == [0, 2, 3, 5, 6, 8, 9, 13], 'incorrect'
