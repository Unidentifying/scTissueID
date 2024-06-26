#############################
#RF
#Run: python3 RF.py example/trains.csv example/trainslabel.csv example/tests.csv example/testslabel.csv ./
#Input args:
#	Input: 
#		Reference tissue: 		',' separated CVS matrix, each row as each cell and each col as each gene
#		Reference tissue type label: 	'\n' separated CSV matrix, each row as cell type name 
#		Test tissue: 			',' separated CVS matrix, each row as each cell and each col as each gene
#		Test tissue type: 		'\n' separated CSV matrix, each row as cell type name
#		Output folder:			directory to generate output files
#	Output: 
#		RFpredlabel.csv:	 	'\n' separated CSV matrix, each row as pred cell type name
#		RFtruelabel.csv: 		'\n' separated CSV matrix, each row as true cell type name
#############################

import	os
import	numpy as np
import	pandas as pd
import	time as tm
from	sys import argv
from	pathlib import Path
from	sklearn.ensemble import RandomForestClassifier

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

RF		= RandomForestClassifier(n_estimators = 50)

traintime	= []
testtime	= []
truelab	= []
pred		= []

y_train	= trainlabels
y_test		= testlabels
        
y_train	= y_train.values.ravel()
y_test		= y_test.values.ravel()

tstart		= tm.time()
RF.fit(train, y_train)
traintime	= tm.time()-tstart

tstart		= tm.time()
predicted	= RF.predict(test)
testtime	= tm.time()-tstart

truelab.extend(y_test)
pred.extend(predicted)

truelab	= pd.DataFrame(truelab)
pred		= pd.DataFrame(pred)

Output		= Path(Output)

truelab.to_csv(str(Output/Path("RFtruelabel.csv")), index = False)
pred.to_csv(str(Output/Path("RFpredlabel.csv")), index = False)    
print("Training Time:\t",traintime," s")
print("Test Time:\t",testtime," s")


