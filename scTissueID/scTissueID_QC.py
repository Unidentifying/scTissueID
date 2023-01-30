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

import	os
import	numpy as np
import	pandas as pd
import	time as tm
from	sys import argv
from	pathlib import Path
from	sklearn.svm import LinearSVC
from	sklearn.calibration import CalibratedClassifierCV

Traindata	= argv[1]
Trainlabel	= argv[2]
Testdata	= argv[3]
Testlabel	= argv[4]
Output		= argv[5]

train		= pd.read_csv(Traindata, index_col=0, sep=',')
trainlabels	= pd.read_csv(Trainlabel, header=0, index_col=None, sep=',')
    
test		= pd.read_csv(Testdata, index_col=0,sep=',')
testlabels	= pd.read_csv(Testlabel, header=0, index_col=None, sep=',')

train		= np.log1p(train)
test		= np.log1p(test)
 
scTissueID_QC	= CalibratedClassifierCV(LinearSVC())

traintime	= []
testtime	= []
truelab	= []
pred		= []
prob		= []

y_train	= trainlabels
y_test		= testlabels
        
y_train	= y_train.values.ravel()
y_test		= y_test.values.ravel()

tstart		= tm.time()
scTissueID_QC.fit(train, y_train)
traintime	= tm.time()-tstart

tstart		= tm.time()
predicted	= scTissueID_QC.predict(test)
probability	= np.max(scTissueID_QC.predict_proba(test), axis = 1)
testtime	= tm.time()-tstart

truelab.extend(y_test)
pred.extend(predicted)


truelab	= pd.DataFrame(truelab)
pred		= pd.DataFrame(pred)
probability	= pd.DataFrame(probability)

Output		= Path(Output)
probability.to_csv(str(Output/Path("scTissueIDprobability.csv")), index = False)    

print("Estimation Time:\t",traintime+testtime," s")



