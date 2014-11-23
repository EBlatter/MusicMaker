import sys
from parser import MusicParser
from semantics import MusicSemantics

def main():
	parser = MusicParser()
	interpreter = MusicSemantics(sys.argv[1])
	parsedNotes = parser.parse(sys.argv[1])
	interpreter.createSong(parsedNotes)



if __name__ == '__main__':
	main()