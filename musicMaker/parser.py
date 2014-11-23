import re, fileinput
import pyPEG
import pyparsing
from pyparsing import *

from mmap import mmap,ACCESS_READ
from xlrd import open_workbook

class MusicParser:

	def __init__(self):
		self.pitch = pyparsing.Word(pyparsing.nums)
		self.word = pyparsing.Word(pyparsing.alphanums)
		self.volume = pyparsing.Word(pyparsing.nums)

		self.note = pyparsing.Group(self.pitch  + self.word  + self.volume)
		self.song = pyparsing.OneOrMore(self.note)


	def extractFromExcel(self, filename):
		'''extracts relevant info about fonts and strings from it
			to pass to the actual parser'''
		wb = open_workbook(filename, formatting_info = True)
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
					columnValues.append(str(s.cell(row,col).value))

					if s.cell(row,col).value != '':
						columnValues.append((str(s.cell(row,col).value), str(font.height))) 
						notes = notes + (str(row) + ' ' + str(s.cell(row,col).value) + ' ' + str(font.height) + '\n')
				# print columnValues
				# print
		return notes

	def parse(self, filename):
		'''takes in a .xls file, finds the notes in it and parses relevant information
			and puts it in a nice list'''
		notes = self.extractFromExcel(filename)
		parsedNotes = self.song.parseString(notes)
		print 'parsed:', parsedNotes
		return parsedNotes
