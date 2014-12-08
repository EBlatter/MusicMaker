import os

currentPath = os.path.abspath(__file__)
currentPath = os.path.split(currentPath)[0]
xlrdPath = currentPath.replace('MusicMaker', 'xlrd-0.9.3')
MIDIUtilPath = currentPath.replace('MusicMaker', 'MIDIUtil-0.89')
pypegPath = currentPath.replace('MusicMaker', 'pyPEG2-2.15.0')

os.chdir(xlrdPath)
os.system('python setup.py install')

os.chdir(MIDIUtilPath)
os.system('python setup.py install')

os.chdir(pypegPath)
os.system('python setup.py install')
