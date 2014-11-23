from musicMaker.parser import MusicParser
import sys

def main():
	print 'before parser'
	parser = MusicParser()
	print 'after parser'
	print parser.parse(sys.argv[1])


if __name__ == '__main__':
	main()