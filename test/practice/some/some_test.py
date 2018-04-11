import os

_get_abs_path = lambda path: os.path.normpath(os.path.join(os.getcwd(), path))

print(_get_abs_path)
