# tests to see how to get information about text and formatting from
# excel files. NOTE: it only runs on .xls files, so I may need to convert
# files into .xls files in case that's not what the user uses. 
# output shows information for each column in a sheet, including the font
# size for any word in the column, as well as where in each column it is.
# words later in the list (has more commas in front of it) will have lower
# pitches because they are lower in the column.

from mmap import mmap,ACCESS_READ
from xlrd import open_workbook

wb = open_workbook('test.xls', formatting_info = True)
xflist = wb.xf_list
fonts = wb.font_list

for s in wb.sheets():

	for col in range(s.ncols):
		#print 'note #', col
		values = []
		sizes = []
		for row in range(s.nrows):

			#get information for font size
			xfx = s.cell_xf_index(row, col)
			font = fonts[xflist[xfx].font_index]
			values.append(str(s.cell(row,col).value))
			#if values[-1] != '':
				#print 'font size for ', values[-1], ' is: ', font.height
				#print font.dump()
			sizes.append(str(font.height))

		print ','.join(values)
		print
		#print ','.join(sizes)
	print


# f = open('test.xlsx')
# print f.read()