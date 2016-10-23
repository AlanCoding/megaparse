import yaml
import json
from megaparse.parsers import parse_kv

__all__ = ['load', 'loads']

def load(stream):
	try:
		ret = json.loads(stream)
	except:
		try:
			ret = yaml.load(stream)
			assert type(ret) is dict
		except:
			try:
				ret = parse_kv(stream)
			except:
				ret = {}
	return ret


loads = load
