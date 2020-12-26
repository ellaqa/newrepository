import sys
import subprocess
from subprocess import STDOUT
import pytest


@pytest.mark.parametrize("a,b,c, expected",
                         [('3', '3', '3', 'equilateral')])
def test_triangle(a, b, c, expected):
    process = subprocess.run(["python3", "triangle_two.py", a, b, c],
                              universal_newlines=True,
                              stdout=subprocess.PIPE)
    assert process.stdout == [expected]
