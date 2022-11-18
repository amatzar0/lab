import pytest
from account import *

class Test:
    def setup_method(self):
        self.a1 = Account('Alex')
        self.a2 = Account('Natalia')

        self.a1.deposit(30)
        self.a2.deposit(62)

    def teardown_method(self):
        del self.a1
        del self.a2
    
    def test_init(self):
        assert self.a1.get_name() == 'Alex'
        assert self.a1.get_balance() == 30

        assert self.a2.get_name() == 'Natalia'
        assert self.a2.get_balance() == 62

    def test_deposit(self):
        assert self.a1.deposit(-5) is False
        assert self.a1.deposit(0) is False
        assert self.a1.deposit(10) is True

        assert self.a2.deposit(-20) is False
        assert self.a2.deposit(0) is False
        assert self.a2.deposit(55) is True

    def test_withdraw(self):
        assert self.a1.withdraw(-3) is False
        assert self.a1.withdraw(31) is False
        assert self.a1.withdraw(30) is True

        assert self.a2.withdraw(-32) is False
        assert self.a2.withdraw(63) is False
        assert self.a2.withdraw(62) is True