import os

currentPath = os.path.abspath(__file__)
currentPath = os.path.split(currentPath)[0]
currentPath = os.path.split(currentPath)[0]
xlrdPath = os.path.join(currentPath, 'xlrd-0.9.3')
MIDIUtilPath = os.path.join(currentPath, 'MIDIUtil-0.89')
pypegPath = os.path.join(currentPath, 'pyPEG2-2.15.0')

os.chdir(xlrdPath)
os.system('python setup.py install')

os.chdir(MIDIUtilPath)
os.system('python setup.py install')

os.chdir(pypegPath)
os.system('python setup.py install')
