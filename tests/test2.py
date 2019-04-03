import pytest

def add(x,y):
    return x+y

@pytest.mark.parametrize("num1, num2, sum", [(1,1,2), (1,2,3), (2,2,4)])
def test_add(num1,num2,sum):
    assert add(num1,num2) == sum
