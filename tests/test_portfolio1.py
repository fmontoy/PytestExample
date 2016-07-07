# **************py.test**************
import py.test
import sys
from source.portfolio1 import Portfolio


def test_buy_one_stock():
        p = Portfolio()
        p.buy("IBM", 3, 100)
        assert p.cost() == 300
