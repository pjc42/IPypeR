
# make PypeR available at IPypeR package level
from .PypeR import *

from .ipyper import *
from .apyper import *
from .rmagics import *
from .PypeR.pyper import *
from .PypeR.misc_pkg import *


# during dev use dev.pth path file to add additional modules for debug and so on
print('IPypeR imported ....')