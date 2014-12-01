import os

currentPath = os.path.abspath(__file__)
currentPath = os.path.split(currentPath)[0]
xlrdPath = currentPath.replace('musicMaker', 'xlrd-0.9.3')
MIDIUtilPath = currentPath.replace('musicMaker', 'MIDIUtil-0.89')

os.chdir(xlrdPath)
os.system('python setup.py install')

os.chdir(MIDIUtilPath)
os.system('python setup.py install')
