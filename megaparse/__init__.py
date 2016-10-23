import yaml
import json

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
				ret = kv.load(stream)
			except:
				ret = {}
	return ret


loads = load
