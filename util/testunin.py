#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import pytest
def func(x):
    return x + 1


def test_func0():
    assert func(3) == 5

def test_func1():
    assert func(4) == 5

def test_func2():
    assert func(5) == 5

def test_func3():
    assert func(5) == 5

if __name__ == '__main__':
    pytest.main()