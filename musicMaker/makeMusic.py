import os
import sys
from musicparser import *
from semantics import MusicSemantics

def main():
	parser = MusicParser()
	interpreter = MusicSemantics(sys.argv[1])

	parsedNotes = parser.parse(sys.argv[1])
	interpreter.createSong(parsedNotes)

	currentPath = os.path.abspath(__file__)
	currentPath = os.path.split(currentPath)[0]
	songPath =  os.path.join(currentPath, sys.argv[1] + '.mid')
	os.system('open \'' +songPath + '\'')



if __name__ == '__main__':
	main()