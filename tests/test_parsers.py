import megaparse

def test_correct_yaml():
	astr = "a: 4"
	assert megaparse.load(astr)['a'] == 4