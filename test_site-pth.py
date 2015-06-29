__author__ = 'pjc'

import site
import sys

site.addpackage('.', 'myLib.pth', None)

for path in sys.path:
    print(path)