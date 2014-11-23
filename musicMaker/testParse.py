from parser import MusicParser
import sys

def main():
	parser = MusicParser()
	parser.parse(sys.argv[1])


if __name__ == '__main__':
	main()