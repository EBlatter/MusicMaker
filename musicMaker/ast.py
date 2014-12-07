from pypeg2 import *

number = re.compile("\d+")
vowel = re.compile("[aeiouy]+")
consonant = re.compile("[^aeiouy\s]+")
notWhitespace = re.compile("[^\s]+")

class Pitch(int):
	grammar = number

class Volume(float):
	grammar = number

class Vowels(List):
	grammar = contiguous(maybe_some([vowel, omit(consonant)]))

class Note(str):
	grammar = attr("pitch", Pitch), attr("vowels", Vowels), attr("volume", Volume)

class Song(List):
	grammar = maybe_some(Note)

#re.match("(?P<vowel>[aeiou])(?P=vowel)+","ae").group()