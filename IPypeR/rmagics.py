from __future__ import print_function
__author__ = 'pjc'

# To get the cell magics to work you need to hold the R process in state so you can call the
# same process each time without reinitializing and getting a new R process. You may want a new
# R process but it should be optional not mandatory each time you call a cell magic

# ref: https://ipython.org/ipython-doc/dev/config/custommagics.html

# This code can be put in any Python module, it does not require IPython
# itself to be running already.  It only creates the magics subclass but
# doesn't instantiate it yet.

from IPython import get_ipython

import IPypeR.PypeR.pyper as pyper


from IPython.core.magic import (
    Magics, magics_class, line_magic, cell_magic, line_cell_magic
    )

@magics_class
class RProcess(Magics):
    """
    A stateful magic class
    Is initialized with a connection to a PypeR R process
    and holds this in state so it can be used across cell magic calls
    """

    # there will always be at least R process, the default_r_process
    default_r_process = None
    path_to_default_r_process = None
    # may create additional named R processes, store in dict
    rProcesses = {}
    rPaths = {}

    def __init__(self, shell, path_to_r_exe):
        # You must call the parent constructor
        super(RProcess, self).__init__(shell)

        pyper_r = pyper.R(RCMD=path_to_r_exe)
        self.default_r_process = pyper_r
        self.path_to_default_r_process = path_to_r_exe

    @cell_magic
    def cmagic(self, line, cell):
        "my cell magic"
        return line, cell

    @line_cell_magic
    def lcmagic(self, line, cell=None):
        "Magic that works both as %lcmagic and as %%lcmagic"
        if cell is None:
            print("Called as line magic")
            return line
        else:
            print("Called as cell magic")
            return line, cell

    @cell_magic
    def r(self, line, cell):
        "my cell magic"
        if line is None:
            self.default_r_process.run(cell)
        return line, cell


# factory method to create and register RProcess object
# the RProcess object has to be a singleton because the cell and line magic methods
# are registered by their name and thus creating multiple objs just overwrites the
# existing cell/line magics
def create_IPypeR(path_to_r_exe=None):
    """
    createIPypeR(path_to_r_exe = <path-to-R.exe>)
        creates and registers IPypeR magics with default process attached to <path-to-R.exe>
        returns the objRProcess, a RProcess class, subclass of magics_class

    you get access to the underlying PypeR process using:

        objRProcess.default_r_process, or
        objRProcess.rProcesses['nameOfRProcess']

    use the standard methods on the PypeR obj to pass data to and from

    use the following convenience magics to run R code

      %%RScript [<RProcessName>]


    :param path_to_r_exe:
    :return: RProcess obj, a magics_class
    """

    #TODO this is a hack during development, should fail and return help message
    if not path_to_r_exe:
        path_to_r_exe='B:\\bin\\r\\App\\R-Portable\\bin\\R.exe'

    # TODO this will raise an exception and needs to be wrapped in try/catch
    check_r_path(path_to_r_exe)

    ip = get_ipython()
    rmagic = RProcess(ip, path_to_r_exe)
    # register RProcess class and its cell/line magics with the IPython kernel
    ip.register_magics(rmagic)

    # return the rmagic obj so it can be used to access underlying PypeR objs
    # and other utils
    return rmagic




#####################################################################################
#   helper functions
#####################################################################################
import os.path


def check_r_path(the_path):

    if not os.path.isfile(the_path):
        raise ValueError('Invalid path to R.exe', the_path)

    basename = os.path.basename(the_path)
    if not basename.lower() == 'r.exe':
        raise ValueError('Invalid path to R.exe, expect path to lead to R.exe', the_path, basename)


