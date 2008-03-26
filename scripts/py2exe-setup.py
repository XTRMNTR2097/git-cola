from distutils.core import setup
import py2exe

setup(
	windows = [
		{"script" : "git-ugit.py"},
	],
	options = {
		"py2exe" : {
			"includes" : ["PyQt4._qt", "pprint", "sip"],
		}
	}
)
