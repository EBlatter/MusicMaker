from ast import *
from mmap import mmap,ACCESS_READ
from xlrd import open_workbook
import warnings

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
						word = str(s.cell(row,col).value).lower()
						columnValues.append((word, str(font.height))) 
						
						if len(columnValues) > 1:
							warnings.warn("Column " + str(col + 1) + " has more than one note in it. The notes will be played sequentially, not at the same time.")

						notes = notes + (str(row) + ' ' + word + ' ' + str(font.height)+'\n')

				#case where a column is left empty to designate a rest
				if columnValues == []:
					notes = notes + ('0 - 0\n')
		# print notes
		return notes

	def parse(self, filename):
		'''takes in a .xls file, finds the notes in it and parses relevant information
			and puts it in a nice list'''
		notes = self.extractFromExcel(filename)
		song = parse(notes, Song)
		return song
