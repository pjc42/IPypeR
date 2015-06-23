# IPypeR

## WIP -- incomplete not working

The *main* lib for calling R from IPython appears to be [rpy2](http://rpy.sourceforge.net/) 
([rpy2 source](https://bitbucket.org/rpy2)). rpy2 uses its own C lib of functions of interact with R from python and
as a consequence must be compiled for each platform. As of 6/2015 I was not able to find an easy way to compile for 
Windows x64. 
 
PypeR is an alternate lib for using R from python. 
[PypeR](http://www.webarray.org/softwares/PypeR/) (PYthon-piPE-R, originally names as Rinpy - R in Python) 
allows people to use R in Python through PIPE. It is a pure python lib so is easily used across platforms and 
may have some other advantages also, see the author's description [here](http://www.jstatsoft.org/v35/c02/paper). 

PypeR can be downloaded:

* [PyPI](https://pypi.python.org/pypi/PypeR/)
* [SourceForge](http://sourceforge.net/projects/rinpy/)




See python calling R via pipes, ref: http://www.webarray.org/softwares/PypeR/

 
IPypeR adds some auxilary functions to PypeR to make it more convenient to use from an IPython notebook.

This is a project to play around with some convenience wrappers for use of the PypeR lib in IPython notebook


PypeR is the core lib with all of the functionality for interacting with R from python
IPypeR is a set of auxillary functions and line and cell magics to make it more convenient to use PypeR from IPython notebook.

##TODO
* create line and cell magics to simplify use
* handle graphics gracefully, i.e. automatically wrap R plot in external png files


### examples

#### init

	R = newRProcess(< usual args>)

#### run some R code

	%%runR <R-process-object-initialized>

	<the cell is then passed as a string of commands to R>

#### pass some data back and forth

use the standard PypeR API

#### run a R graph

	%%runRGraph

	<the cell with all the R graphics code>

The cell is then passed as a string of commands to R, wrapped in png() and dev.off() (to close the png file). It also appends python call to Image() to display png() file in the notebook.

Note that one problem with this workflow is that the png graph is not saved in the notebook (or is it, check this)