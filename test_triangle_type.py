import sys
import subprocess
from subprocess import STDOUT
import pytest


@pytest.mark.parametrize("a,b,c, expected",
                         [(3, 4, 5, 'scalene')])
def test_triangle(a, b, c, expected):
    subprocess.run(args=[a, b, c],universal_newlines=True,STDOUT=subprocess.PIPE)
assert STDOUT == ['expected']
