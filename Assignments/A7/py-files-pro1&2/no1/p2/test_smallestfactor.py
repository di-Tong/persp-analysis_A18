#test_smallestfactor.py

import smallestfactor

def test_smallestfactor():
	assert smallestfactor.smallest_factor(121) == 11, "incorrect result"
	assert smallestfactor.smallest_factor(1) == 1, "incorrect result"
	assert smallestfactor.smallest_factor(7) == 7, "incorrect result"