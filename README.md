# scTissueID


This is scTissueID for cell type annotation.


Install:

Requirements:

    Cython >=0.23
    Python >= 3.4
    NumPy >= 1.8.2
    SciPy >= 0.13.3

Install dependencies:
sudo apt-get install build-essential python3-dev python3-setuptools \
                     python3-numpy python3-scipy libatlas-dev \
                     libatlas3-base python-matplotlib

cd ./utils/scTissueID_utils

sudo python3 setup.py install

sudo pip3 install --editable .


Test run

sudo python3 ../../scTissueID.py ../../example/trains.csv ../../example/trainslabel.csv ../../example/tests.csv ../../example/testslabel.csv ../../example



scTissueID.py
Tissue identfication by scTissue
#############################
#scTissueID
#Run: python3 scTissueID.py example/trains.csv example/trainslabel.csv example/tests.csv example/testslabel.csv ./
#Input args:
#	Input: 
#		Reference tissue: 		',' separated CVS matrix, each row as each cell and each col as each gene
#		Reference tissue type label: 	'\n' separated CSV matrix, each row as cell type name 
#		Test tissue: 			',' separated CVS matrix, each row as each cell and each col as each gene
#		Test tissue type: 		'\n' separated CSV matrix, each row as cell type name
#		Output folder:			directory to generate output files
#	Output: 
#		scTissueIDpredlabel.csv: 	'\n' separated CSV matrix, each row as pred cell type name
#		scTissueIDtruelabel.csv: 	'\n' separated CSV matrix, each row as true cell type name
#############################
			
			
scTissueID_QC.py
Quality Control by probability assignment, cells probability greater than 0.8 considered as passed QC as default setting
#############################
#QC
#Run: python3 scTissueID_QC.py example/trains.csv example/trainslabel.csv example/tests.csv example/testslabel.csv ./
#Input args:
#	Input: 
#		Reference tissue: 		',' separated CVS matrix, each row as each cell and each col as each gene
#		Reference tissue type label: 	'\n' separated CSV matrix, each row as cell type name 
#		Test tissue: 			',' separated CVS matrix, each row as each cell and each col as each gene
#		Test tissue type: 		'\n' separated CSV matrix, each row as cell type name
#		Output folder:			directory to generate output files
#	Output: 
#		scTissueIDprobability.csv: 	'\n' separated CSV matrix, each row as the QC probability of each cell type 
#						The rows of test file or cells of QC Probability > 0.8 passed QC
#############################
 
KNN.py LDA.py NMC.py RF.py are baseline algorithms
#############################
#KNN
#Run: python3 KNN.py example/trains.csv example/trainslabel.csv example/tests.csv example/testslabel.csv ./
#Input args:
#	Input: 
#		Reference tissue: 		',' separated CVS matrix, each row as each cell and each col as each gene
#		Reference tissue type label: 	'\n' separated CSV matrix, each row as cell type name 
#		Test tissue: 			',' separated CVS matrix, each row as each cell and each col as each gene
#		Test tissue type: 		'\n' separated CSV matrix, each row as cell type name
#		Output folder:			directory to generate output files
#	Output: 
#		KNNpredlabel.csv:	 	'\n' separated CSV matrix, each row as pred cell type name
#		KNNtruelabel.csv: 		'\n' separated CSV matrix, each row as true cell type name
#############################

example folder contains a short example for input data, where each row contains the profiling of one cell and each column is one gene the matrix is the profile of multiple cells

trainslabel.csv and testslabel.csv includes the cell type labels from collected data as ith row is the cell type of ith cell in trains.csv and tests.csv

Note: training data in example is short (100 cells), might not reflect accuracy.
Please refer to the manuscript for the public available data sets.


