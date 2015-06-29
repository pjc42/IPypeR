__author__ = 'pjc'

# These are all the notebook related convenience methods

# IPypeR.PypeR is the original PypeR project
import IPypeR.PypeR.pyper as pyper

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



def RProcess(pathToRExecutable=None):
    """
    returns a new RProcess (PypeR) class obj
    e.g.
        rprocess = RProcess('B:\\bin\\R.exe')
    :param pathToRExecutable: string
    :return: R obj
    """

    if pathToRExecutable == None:
    # TODO, this is just a hack for dev on Windows
        pathToRExecutable='B:\\bin\\r\\App\\R-Portable\\bin\\R.exe'
        # print_RProcess_Usage()

    r = pyper.R(RCMD=pathToRExecutable)
    return r

@register_cell_magic
# %%rproc
def rproc(line, cell):
    # We create a string buffer containing the
    # contents of the cell.
    sio = StringIO(cell)
    # use R proc process R
    print(sio)
    print(type(line), line)
    myr = exec(line)
    print('r.has_numpy: {}'.format(r.has_numpy))
    print('r.has_pandas: {}'.format(r.has_pandas))
    return None

#####################################################################################
#   helper functions
#####################################################################################
def print_RProcess_Usage():
    print('Must provide path to R.exe')
    print('Usage: rprocess = RProcess(\'B:\\bin\\R.exe\') ')



print('ipyper.py evaluated...')