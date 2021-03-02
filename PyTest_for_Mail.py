import pytest
import math

def fib(a):
    if a==0:
        return 1
    elif a==1:
        return 1
    else:
        return fib(a-1)+fib(a-2)


#����� ��� int

#�������� �� ����� �����
@pytest.mark.xfail()
def test_type():
    assert type('a')==type(2)

#�������� �� ��� ����������
def test_year():
    year=2020
    assert ((year%4==0 and year%100!=0) or year%400==0) == True

#������ �� ����� � ������������������ ���������
def test_fib():
    tlst=[1,5,89,10946]
    for i in tlst:
        a=0
        while i>fib(a):
            a+=1
        assert i == fib(a)

#����� ��� float

#������ �� �����, ��� pi
def test_pi():
    a=5.5
    assert a>math.pi

#� ����� �� ����������� ��������
@pytest.mark.xfail()
def test_temp():
    t=99.9
    assert t<39.9


#��������� �� ����� ����� � ������� (����� < 10)
def test_float():
    a=[1.1,3.3,6.6,9.9]
    for i in a:
        i_cell=int(i)
        i_drob=round((i % 1)*10)
        assert i_cell==i_drob
    

