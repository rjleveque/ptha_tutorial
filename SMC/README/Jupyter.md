# Jupyter notebooks

### Workshop on Mapping Uncertain Hazard Information


For general information on Jupyter notebooks, see http://ipython.org/ and https://jupyter.org/.

For many cool examples of notebooks, see:
 - [nbviewer](http://nbviewer.ipython.org/) (which can be used to view static notebooks on the web)
 - [Gallery of interesting notebooks](https://github.com/ipython/ipython/wiki/A-gallery-of-interesting-IPython-Notebooks)
 
Jupyter notebooks end with the extension `.ipynb` (a holdover from when they were called IPython notebooks).  To open an existing notebook, you can just navigate to it from the `Files` menu and click on it, or navigate to the directory in a terminal window and type 

```
open filename.ipynb
```

You can create a new notebook using the latter approach, or click on the `New` tab and then on `Jupyter notebook`.
 
Notebooks generally contain both "code cells" that have executable code (Python, for example, although Jupyter notebooks also support other languages such as Julia and R -- hence the name), and "markdown cells" that contain the text you see between code cells.

For most notebooks we'll use, the first code cell contains only: 

```
%pylab inline
```

This loads a lot of scientific Python modules, and instructs the notebook to display plots inline (in the notebook, rather than trying to open a separate plot window).

Execute a cell by first clicking on the cell and then hitting `Shift-Enter` (hold down Shift while typing Enter on your keyboard).  Or you can select `Run` from the `Cell` menu at the top of the notebook but `Shift-Enter` is simpler.  

You can also try changing values in other code cells and re-execute to create new versions of some of the plots.  But note that what's computed in one cell might depend on things defined in earlier cells, so if you want to do this you should start at the top and first execute all previous cells.  (Note: you can select `Run all` from the `Cell` menu if you want to execute all the cells sequentially, and various other options are there as well, e.g. to execute all cells above the one currently selected.)

If you want to modify a markdown cell, double click on it so you see the input (in the GitHub flavored [markdown](https://help.github.com/articles/markdown-basics/) language, also used in the document you are now reading).   To execute the cell and see the output (nicely formatted text) instead of the input, simply type `Shift-Enter` as usual.
