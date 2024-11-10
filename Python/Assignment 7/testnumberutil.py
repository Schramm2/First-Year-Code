"""Matthew Schramm
2022/01/12
DocString to show 8 test cases that achieve all path coverage in the numberutil program

>>> import numberutil
>>> numberutil.aswords(100) 
'one hundred'
>>> numberutil.aswords(50) 
'fifty'
>>> numberutil.aswords(1) 
'one'
>>> numberutil.aswords(999) 
'nine hundred and ninety nine'
>>> numberutil.aswords(101) 
'one hundred and one'
>>> numberutil.aswords(0) 
'zero'
>>> numberutil.aswords(137) 
'one hundred and thirty seven'
>>> numberutil.aswords(99) 
'ninety nine'





"""
import doctest
doctest.testmod(verbose=True)