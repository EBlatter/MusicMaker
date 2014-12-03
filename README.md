# MusicMaker

##   How to install and run
From the command line, navigate to the musicMaker folder and run setup.py. This should install most of the libraries you need to run the program. The only other library you will need is pyparsing, and installation instructions can be found [here](http://pyparsing.wikispaces.com/Download+and+Installation).

Once you've done that, you can create a program in Excel to run. Save it somewhere in the musicMaker directory. You can then type `python makeMusic.py [ filename ]` to run it. If the file is within a folder in the musicMaker directory (for example, 'call me maybe.xls' in sampleprograms), then make sure to include the path in the filename (for example, `python makeMusic.py sampleprograms/call_me_maybe`).

**IMPORTANT:** Make sure that you save your file as a .xls file, as it will not work with any other type of spreadsheet.

The output should be a MIDI file, which you can then run in any MIDI player to see how it sounds!



<!--See the 
[project requirements](http://www.cs.hmc.edu/~benw/teaching/cs111_fa14/project.html) 
for instructions on setting up your project.
-->