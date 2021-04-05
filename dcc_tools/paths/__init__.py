"""
path tools
"""

import os

def norm_path(path):
	"""
	normalize paths to unix style paths

	Args:
	    path (TYPE): Description
	
	Returns:
	    TYPE: Description
	"""

	if path.startswith('/c/'):
		path = path.replace('/c/', 'c:/')

	return path