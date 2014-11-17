# Language design and implementation overview

## Language design

**How does a user write programs in your language (e.g., do they type in commands, use a visual/graphical tool, speak, etc.)?**

The user will use Excel as a graphical tool to write a program in the language. 

**What is the basic computation that your language performs (i.e., what is the computational model)?**

My language translates specially formatted text into music.  

**What are the basic data structures in your DSL, if any? How does a the user create and manipulate data?**

The basic data structure in my DSL is a note. The user creates on by putting text into a cell in a spreadsheet. Changing the position of the text within a column will alter its pitch, where higher up words will create higher pitches. Changing the size of the text change the volume of the note. At the moment, the plan for determining the length of a note will be based on the number of times a vowel is repeated in a row in a word. However, this plan may change based on some tests with the nltk library, which may be able to find syllable breaks in words.

**What are the basic control structures in your DSL, if any? How does the user specify or manipulate control flow?**

There are no control structures in my DSL. The language is executed from left to right, no matter what the user does.

**What kind(s) of input does a program in your DSL require? What kind(s) of output does a program produce?**

My DSL requires text input. If I decide to base the length of a note on the number of vowels, then there will be no restrictions on what characters can be in a word. This is because non-vowel characters will simply be ignored except to determine breaks between notes. However, if I do find something that can separate syllables, then the input may need to resemble English words more, which would restrict characters to the English alphabet. Currently, I've figured out how to easily write to a MIDI file as output using the MIDIUtils library, so that is the output.

**Error handling: How can programs go wrong, and how does your language communicate those errors to the user?**

It is difficult for the program to go wrong. The main error I can see happening is the user inputing something that can't be broken into notes. With the vowel heuristic method of finding length of notes, a user might not put any vowels in one of the cells, which would make it not a note. My language would throw an error while trying to parse this, showing which section of text doesn't have enough vowels. It's also possible that a user try to put in a larger range of notes than I can create in a MIDI file, so my language should throw an error while parsing.

**What tool support (e.g., error-checking, development environments) does your project provide?**

The user can use Excel to create programs in my language.

**Are there any other DSLs for this domain? If so, what are they, and how does your language compare to these other languages?**

There are a lot of DSLs for describing music. For example, there are a lot of languages, libraries, and tools [here](https://wiki.python.org/moin/PythonInMusic) for creating music with Python. The notation used to create sheet music can also be considered a DSL. My goal with my DSL is to simplify the creating music process a bit to make it more accessible to people who can't read music or program.


## Language implementation

**Your choice of an internal vs. external implementation and how and why you made that choice.**

I chose to implement my language as an external language. My language didn't really make sense to me as an internal language. Making it external gives me more freedom in my syntax, which can help me keep it simple for the users and let them use Excel to create their programs.

**Your choice of a host language and how and why you made that choice.**

I chose Python as my host language. I found several tools in Python that seemed like they would make my implementation process simpler. Sisi showed me a parser for Python that seems very simple to use, and I've found libraries for parsing Excel files and creating MIDI files. I'm also fairly comfortable with using Python, so it seemed like it was a suitable choice. However, any language that has adequate support libraries for Excel files, parsing, and creating music output would have worked as a host language for my DSL.

**Any significant syntax design decisions you've made and the reasons for those decisions.**

I've decided that the location in a column will determine the pitch of a note, its font size will determine its volume, and the number of vowels will determine its 

**An overview of the architecture of your system.**

The architecture of my system will be similar to the architecture in the external Piconot assignment with a parser, intermediate representation, and an evaluator. Keeping them separate is important so that if I decide to change something about the form of the input or the output, the rest of the system can stay in place.

