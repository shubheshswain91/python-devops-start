# Importing the math and pytest libraries
import math
import pytest

# Creating the common function for input
@pytest.fixture
def input_value():
   input = 8
   return input

# Creating first test case
def test_check_difference(input_value):
   assert 99-91==input_value

# Creating second test case
def test_check_square_root(input_value):
   assert input_value==math.sqrt(64)