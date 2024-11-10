"""Matthew Schramm
2022/01/12
DocString to show 6 test cases that achieve all statement coverage in the timeutil program

>>> import timeutil
>>> timeutil.validate(":15 a.m.")
False
>>> timeutil.validate("102:15 a.m.")
False
>>> timeutil.validate("02:15 a.m.")
False
>>> timeutil.validate("15:15 z.m.")
False
>>> timeutil.validate("12:59 a.m.")
True
>>> timeutil.validate("12:102 a.m.")
False





"""
import doctest
doctest.testmod(verbose=True)