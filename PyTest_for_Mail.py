import pytest

def add(a):
    return a+1

def test_loop():
    for i in range(3):
        assert add(i)==i+1

def test_one():
    assert (1,2,3)==(1,2,3)

@pytest.mark.skip()
def test_two():
    assert (1,2,3)==(3,2,1)

@pytest.mark.xpass()
def test_three():
    assert add(3)==4

@pytest.mark.xfail()
def test_four():
    assert add(3)==5