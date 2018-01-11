#!/usr/bin/env python
# _*_ coding: utf-8 _*_

# content of test_time.py
import pytest
from datetime import datetime, timedelta

testdata = [
    (datetime(2001, 12, 12),datetime(2001, 12, 11),timedelta(1)),
    (datetime(2001, 12, 11), datetime(2001, 12, 11), timedelta(-1)),
]

@pytest.mark.parametrize("a,b,expected", testdata)
def test_timedistance_v0(a, b, expected):
    diff = a - b
    assert diff == expected

@pytest.mark.parametrize("a,b,expected", testdata, ids=["forward", "backward"])
def test_timedistance_v1(a, b, expected):
    diff = a - b
    assert diff == expected

def idfn(val):
    if isinstance(val, (datetime,)):
        # note this wouldn't show any hours/minutes/seconds
        return val.strftime('%Y%m%d')

@pytest.mark.parametrize("a,b,expected", testdata, ids=idfn)
def test_timedistance_v2(a, b, expected):
    diff = a - b
    assert diff == expected


# pytest  test.py --html=html_path_name