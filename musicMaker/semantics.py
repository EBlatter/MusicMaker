#Import the library
from midiutil.MidiFile import MIDIFile

class PitchValueError(Exception):
     def __init__(self, value):
         self.value = value
     def __str__(self):
         return repr(self.value)

class NoteDurationError(Exception):
	 def __init__(self, value):
	     self.value = value
	 def __str__(self):
	     return repr(self.value)


class MusicSemantics:

	def __init__(self, trackName = 'MusicMakerSong'):
		self.trackName = trackName
		# Create the MIDIFile Object with 1 track
		self.file = MIDIFile(1)

		# Tracks are numbered from zero. Times are measured in beats.
		self.track = 0
		self.time = 0

		# Add track name and tempo.
		self.file.addTrackName(self.track,self.time,trackName)
		self.file.addTempo(self.track,self.time,240)

		#start pitch and volume that everything else will be relative to
		self.pitch = 71
		self.maxVol = 0

		self.vowels = ['a','e','i','o','u','y']

	def addNote(self, note):
		duration = self.findMaxVowelsNote(note.vowels)
		if duration == 0:
			if note.vowels == []:
				raise NoteDurationError("Song has a note with no vowels, so duration cannot be determined. Please add vowels.")

		# error handling for note pitch limits
		if note.pitch >= self.pitch+1:
			raise PitchValueError("Pitch in row " + str(note.pitch + 1) + " is too low. Try moving it to row " + str(self.pitch) + " or higher.")
		
		# Add a note. addNote expects the following information:
		track = 0
		channel = 0
		pitch = self.pitch - note.pitch
		volume = 100.0*(note.volume/self.maxVol)

		# notes are inaudible in some programs if they're less than 25.
		if volume < 25.0:
			volume = 25.0

		# Now add the note.
		self.file.addNote(track,channel,pitch,self.time,duration,volume)

		self.time += duration

	def findMaxVowelsNote(self, vowelList):
		'''finds the longest string of vowels in a note'''
		maxVowels = 0
		for subnote in vowelList:
			maxSubnoteVowels = self.findMaxVowelsSubnote(subnote)
			if maxSubnoteVowels > maxVowels:
				maxVowels = maxSubnoteVowels
		return maxVowels

	def findMaxVowelsSubnote(self, subnote):
		'''finds the longest string of vowels in a subnote (collection of vowels within a note'''
		maxLength = 0
		for vowel in self.vowels:
			count = subnote.count(vowel)
			if maxLength < count:
				maxLength = count
		return maxLength

	def findMaxVolume(self, notes):
		for note in notes:
			if float(note.volume) > self.maxVol:
				self.maxVol = float(note.volume)

	def createSong(self, notes):
		'''takes in parsed notes, creates MIDI file for those notes'''
		self.findMaxVolume(notes)
		for note in notes:
			self.addNote(note)

		# And write it to disk.
		binfile = open(self.trackName+'.mid', 'wb')
		self.file.writeFile(binfile)

		binfile.close()