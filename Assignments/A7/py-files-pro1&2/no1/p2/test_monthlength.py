#test_monthlength.py

import monthlength

def test_monthlength():
	assert monthlength.month_length("September", leap_year=False) == 30, "incorrect result"
	assert monthlength.month_length("March", leap_year=False) == 31, "incorrect result"
	assert monthlength.month_length("February", leap_year=False) == 28, "incorrect result"
	assert monthlength.month_length("February", leap_year=True) == 29, "incorrect result"
	assert monthlength.month_length("Else", leap_year=False) == None, "incorrect result"
