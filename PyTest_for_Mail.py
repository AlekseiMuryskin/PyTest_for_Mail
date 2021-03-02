import pytest
import math

def fib(a):
    if a==0:
        return 1
    elif a==1:
        return 1
    else:
        return fib(a-1)+fib(a-2)


#“есты дл€ int

#€вл€етс€ ли число целым
@pytest.mark.xfail()
def test_type():
    assert type('a')==type(2)

#€вл€етс€ ли год високосным
def test_year():
    year=2020
    assert ((year%4==0 and year%100!=0) or year%400==0) == True

#входит ли число в последовательность ‘ибоначчи
def test_fib():
    tlst=[1,5,89,10946]
    for i in tlst:
        a=0
        while i>fib(a):
            a+=1
        assert i == fib(a)

#тесты дл€ float

#больше ли число, чем pi
def test_pi():
    a=5.5
    assert a>math.pi

#в норме ли температура человека
@pytest.mark.xfail()
def test_temp():
    t=99.9
    assert t<39.9


#совпадает ли цела€ часть с дробной (числа < 10)
def test_float():
    a=[1.1,3.3,6.6,9.9]
    for i in a:
        i_cell=int(i)
        i_drob=round((i % 1)*10)
        assert i_cell==i_drob
    

