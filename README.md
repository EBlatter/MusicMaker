# MusicMaker
The goal of this language is that a program written in it will sound the way it looks, which will not only make it easier to write music, especially for those who can't read typical music notation, and would also be a fun way to make music. In one sentence, my DSL will take in text that is formatted by the user and output music based on characteristics of the text. This language is good for the domain of music because it notates music in a way that takes advantage of the user's intuition about music; in general, longer notes are longer, higher notes are higher, and bigger notes are louder.

## Example programs
Examples can be found in the MusicMaker/sampleprograms directory. The easiest to understand example is batman.xls. Most people are familiar with the Batman theme, and so if you follow along with the position of the notes, you can see that it seems to map to what they would expect of the pitches. The program also gets louder as the song goes on, which can be seen from the text getting bigger from left to right. Also, the last two notes are held out longer than the previous notes, which is why they are 'baaaat' and 'maaaaaaaaaan' rather than 'bat' and 'man'. When this program runs, the output is a MIDI file (called batman.mid), which is placed in the same MusicMaker/sampleprograms directory and should sound like teh Batman theme song.

##   How to install and run
Download the .zip file from GitHub. Then, from the command line, navigate to the MusicMaker folder and run setup.py. This should install the libraries you need to run the program. 

Once you've done that, you can create a program in Excel to run. Save it somewhere in the musicMaker directory. You can then type `python makeMusic.py [ filename ]` to run it. If the file is within a folder in the MusicMaker directory (for example, 'call me maybe.xls' in sampleprograms), then make sure to include the path in the filename (for example, `python makeMusic.py sampleprograms/call_me_maybe`).

**IMPORTANT:** Make sure that you save your file as a .xls file, as it will not work with any other type of spreadsheet.

The output should be a MIDI file, which you can then run in any MIDI player to see how it sounds!

There is also a template file (MusicMaker.xlt) that can be used to make creating music easier. Save this with the rest of your Excel templates, and you can then use it to write songs.



<!--See the 
[project requirements](http://www.cs.hmc.edu/~benw/teaching/cs111_fa14/project.html) 
for instructions on setting up your project.
-->