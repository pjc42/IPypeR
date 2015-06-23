__author__ = 'pjc'

# These are all the notebook related convenience methods

from IPypeR.PypeR import (R)

from IPython.core.magic import (register_line_magic, register_cell_magic)

@register_line_magic
def hello(line):
    if line == 'french':
        print("Salut tout le monde!")
    else:
        print("Hello world!")


import pandas as pd
#from StringIO import StringIO  # Python 2
from io import StringIO  # Python 3

@register_cell_magic
def csv(line, cell):
    # We create a string buffer containing the
    # contents of the cell.
    sio = StringIO(cell)
    # We use Pandas' read_csv function to parse
    # the CSV string.
    return pd.read_csv(sio)



def newR():
    print('wtf')
    rInstallPath='B:\\bin\\r\\App\\R-Portable\\bin\\R.exe'
    r = R(RCMD=rInstallPath)
    print('new r created')
    return r

print('ipyper.py evaluated')
