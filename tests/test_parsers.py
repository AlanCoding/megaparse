import megaparse

def test_correct_yaml():
	astr = "a: 4"
	assert megaparse.load(astr)['a'] == 4

def test_correct_key_value():
	astr = "a=4"
	assert megaparse.parsers.parse_kv(astr)['a'] == 4

def test_key_value_str():
	astr = "a=bannana"
	assert megaparse.parsers.parse_kv(astr)['a'] == 'bannana'

def test_kv_root_level():
	astr = "a=bannana"
	assert megaparse.load(astr)['a'] == 'bannana'
