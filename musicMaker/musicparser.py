from ast import *
from mmap import mmap,ACCESS_READ
from xlrd import open_workbook

class MusicParser:

	def extractFromExcel(self, filename):
		'''extracts relevant info about fonts and strings from it
			to pass to the actual parser'''
		wb = open_workbook(filename+'.xls', formatting_info = True)
		xflist = wb.xf_list
		fonts = wb.font_list
		notes = ""
		for s in wb.sheets():

			for col in range(s.ncols):
				columnValues = []
				sizes = []
				for row in range(s.nrows):
					#get information for font size
					xfx = s.cell_xf_index(row, col)
					font = fonts[xflist[xfx].font_index]

					if s.cell(row,col).value != '':
						columnValues.append((str(s.cell(row,col).value), str(font.height))) 
						# currently stripping off the last letter of the word to avoid current problems with silent e's at the end
						# TODO: deal with this better
						notes = notes + (' ' + str(row) + ' ' + str(s.cell(row,col).value)[:-1] + ' ' + str(font.height))

				#case where a column is left empty to designate a rest
				#TODO: figure out how I want these represented
				if columnValues == []:
					notes = notes + (' 0 - 0')
		notes = notes.lstrip()
		return notes

	def parse(self, filename):
		'''takes in a .xls file, finds the notes in it and parses relevant information
			and puts it in a nice list'''
		notes = self.extractFromExcel(filename)

		song = parse(notes, Song)
		for note in song:
			print 'note'
			print note.subnotes
			print
		return song
