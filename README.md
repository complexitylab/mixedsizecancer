

# The mixed cancer culture model

The notebooks contain the two-dimensional cellular automata model of the mixed cancer culture written in Python. The model demonstrates simultaneous growth of two cancer cell lines (Line1 and Line2). Depending on the objectives, the user can run different versions of the model (note the Jupyter notebook title).

### Cell size

* *"Identical Size"* - the cells of Line1 and Line2 are of the same size
* *"Different Size"* - the cells of Line1 (red) are four-times bigger than these of Line2 (blue)

### Game of Life rules
* *"GoL Conway"* - the game of life rules introduced by John Conway
* *"GoL Maximum Growth"* - the rules allow the cells to proliferate every time a free site is available in the neighborhood and completely exclude the possibility of cell death
* *"GoL Standard"* - the rules intended to simulate closer the real-life cancer behavior
* user-defined game of life rules can be introduced by manually changing the parameters of "GoL" function in "Cell_line1" or "Cell_line2" classes


| GoL rules  <td colspan=2>**standard**   <td colspan=2>**Conway**  <td colspan=2>**maximum growth** |
| :--- | :---: | :---: | :---: | :---: | :---:| :---: |
| state | probability | number of neighbors | probability | number of neighbors |probability | number of neighbors |
| cell dies of loneliness 			| 0.1  | [0, 1] | 1 | [0, 1] | 0 | [0, 1] |
| cell dies from overpopulation  	| 0.5  | [7, 8] | 1 | [4, 8] | 0 | [7, 8] |
| cell stays alive  					| 1    | [2, 6] | 1 | [2, 3] | 1 | [2, 6] |
| cell is born (range 1) 			| 0.25 | [1, 2] | 0 | [1, 2] | 1 | [1, 2] |
| cell is born (range 2) 			| 0.75 | [3, 6] | 1 | [3, 3] | 1 | [3, 6] |
| cell is born (range 3) 			| 0.9  | [7, 8] | 0 | [4, 8] | 1 | [7, 8] |


 

### Parameters setting
The user is asked to enter the following parameters:

* the name for the output files
* custom directory of the output folder
* the lattice size
* the number of cells in the initial population of Line1 and Line2
* the proliferation rate for Line1 (for Line2 the default value is 1)
* the number of iterations  

### How to run
Each notebook contains an independent program. To execute the program use Anaconda distribution of Python and simply run all cells in the notebook. Set the parameters you are asked for. Make sure that all the packages used in the code are installed. Programs were tested with Python 3.7.3 and Anaconda 4.8.2.


### Citation
If you find this code useful in your research, please consider citing: Kłóś A, Płonka P (2020) *Growth of mixed cancer cell population – in silico the size matters*, Acta Biochimica Polonica 67(4). https://doi.org/10.18388/abp.2017_.

	@Article{,
	author = {Kłóś Adam, Płonka Przemysław}, 
	title = {Growth of mixed cancer cell population -- in silico the size matters}, 
	journal = {Acta Biochimica Polonica}, 
	volume = {67}, 
	number = {4}, 
	pages = {}, 
	year = {2020}
	} 