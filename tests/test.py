from projecthack import recursion


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
