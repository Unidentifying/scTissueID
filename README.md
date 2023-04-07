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


Please read detail instruction inside
