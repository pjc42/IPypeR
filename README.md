# PypeR
python calling R via pipes, ref: http://www.webarray.org/softwares/PypeR/

This is a project to play around with some convenience wrappers for use of the PypeR lib in IPython notebook

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