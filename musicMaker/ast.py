from pypeg2 import *

number = re.compile("\d+")
notWhitespace = re.compile("[^\s]+")

class Pitch(int):
	grammar = number

class Volume(float):
	grammar = number

# class Vowels(List):
# 	grammar = 

class Note(str):
	grammar = attr("pitch", Pitch), notWhitespace, attr("volume", Volume)

class Song(List):
	grammar = maybe_some(Note)