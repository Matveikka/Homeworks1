import inspect
from pprint import pprint
def introspection_info(obj):
    _type = type(obj).__name__
    _attr = dir(obj)
    _methods = inspect.getmembers(obj)
    _module = obj.__class__.__module__
    info = {'type': _type, 'attributes': _attr, 'methods': _methods, 'module': _module}
    return info

number_info = introspection_info(7)
pprint(number_info)