import os
from glob import glob

for file in glob(os.getcwd()+'\\*[.xlsx|.csv|.pdf]'):
    os.remove(file)
