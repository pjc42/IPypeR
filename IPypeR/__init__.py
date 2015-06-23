
# make PypeR available at IPypeR package level
from IPypeR.PypeR import *

__all__ = ['ipyper', 'apyper']

from IPypeR.ipyper import *
from IPypeR.apyper import *

from IPypeR.ipyper import newR

print('IPypeR imported ....')