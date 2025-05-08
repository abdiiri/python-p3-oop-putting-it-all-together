import pytest
import io
import sys
from lib.shoe import Shoe  # Make sure this import is correct

class TestShoe:
    def test_has_brand_and_size(self):
        '''Shoe in shoe.py has the brand and size passed to __init__, and values can be set to new instance.'''
        shoe = Shoe("Nike", 10)
        assert shoe.brand == "Nike"
        assert shoe.size == 10
        shoe.brand = "Adidas"
        shoe.size = 9
        assert shoe.brand == "Adidas"
        assert shoe.size == 9

    def test_requires_int_size(self):
        '''prints "size must be an integer" if size is not an integer.'''
        stan_smith = Shoe("Adidas", 9)
        captured_out = io.StringIO()
        sys.stdout = captured_out
        stan_smith.size = "not an integer"
        sys.stdout = sys.__stdout__
        assert "size must be an integer" in captured_out.getvalue()

    def test_can_repair(self):  # Renamed from test_can_cobble
        '''says that the shoe has been repaired.'''
        shoe = Shoe("Puma", 11)
        captured_out = io.StringIO()
        sys.stdout = captured_out
        shoe.repair()
        sys.stdout = sys.__stdout__
        assert "The shoe has been repaired." in captured_out.getvalue()

    def test_repair_makes_new(self):  # Renamed from test_cobble_makes_new
        '''creates an attribute on the instance called 'condition' and set equal to 'New' after repair.'''
        stan_smith = Shoe("Adidas", 9)
        stan_smith.repair()
        assert hasattr(stan_smith, 'condition')
        assert stan_smith.condition == "New"